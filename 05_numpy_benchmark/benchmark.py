"""
Сравнение PostgreSQL SQL vs NumPy на одном и том же dataset.

Установка:
    pip install numpy pandas psycopg[binary]

Запуск:
    python benchmark.py

PostgreSQL:
    host=localhost
    port=5428
    db=benchmark
    user=benchmark
    password=benchmark

Что вычисляем одинаково в обоих вариантах:

    total_revenue =
        SUM(quantity * unit_price * (1 - discount))

    average_order_value =
        AVG(quantity * unit_price * (1 - discount))

    large_sales_count =
        COUNT(*) WHERE quantity * unit_price * (1 - discount) >= 5000

Для NumPy учитываем два времени:
1. fetch + NumPy — получение данных из PostgreSQL + вычисления;
2. pure NumPy — только вычисления после загрузки.

Для SQL отдельно показываем:
1. SQL end-to-end — выполнение запроса PostgreSQL через клиент;
2. execution time из EXPLAIN ANALYZE — время выполнения внутри PostgreSQL.

Так сравнение получается честнее: мы не смешиваем скорость
вычислений с сетевым/десериализационным overhead.
"""

from __future__ import annotations

import statistics
import time

import numpy as np
import psycopg


DB_CONFIG = {
    "host": "localhost",
    "port": 5428,
    "dbname": "benchmark",
    "user": "benchmark",
    "password": "benchmark",
}

REPEATS = 3


SQL_QUERY = """
SELECT
    SUM(quantity * unit_price * (1 - discount)) AS total_revenue,
    AVG(quantity * unit_price * (1 - discount)) AS average_order_value,
    COUNT(*) FILTER (
        WHERE quantity * unit_price * (1 - discount) >= 5000
    ) AS large_sales_count
FROM sales;
"""


def percentile(values: list[float], p: float) -> float:
    return float(np.percentile(values, p))


def print_stats(name: str, values: list[float]) -> None:
    print(f"\n{name}")
    print("-" * len(name))
    print(f"min:    {min(values):.4f} s")
    print(f"median: {statistics.median(values):.4f} s")
    print(f"p95:    {percentile(values, 95):.4f} s")


def get_sql_result(conn):
    with conn.cursor() as cur:
        cur.execute(SQL_QUERY)
        row = cur.fetchone()

    return {
        "total_revenue": float(row[0]),
        "average_order_value": float(row[1]),
        "large_sales_count": int(row[2]),
    }


def run_sql_benchmark() -> tuple[dict, list[float]]:
    times = []
    result = None

    with psycopg.connect(**DB_CONFIG) as conn:
        # Один прогрев.
        result = get_sql_result(conn)

        for _ in range(REPEATS):
            started = time.perf_counter()
            result = get_sql_result(conn)
            elapsed = time.perf_counter() - started
            times.append(elapsed)

    return result, times


def load_numpy_data():
    """
    Загружаем только столбцы, необходимые для вычисления.
    PostgreSQL остаётся источником данных.
    """
    with psycopg.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                SELECT
                    quantity,
                    unit_price,
                    discount
                FROM sales
                """
            )

            rows = cur.fetchall()

    # Преобразование в NumPy-массивы.
    data = np.asarray(rows, dtype=np.float64)

    quantity = data[:, 0]
    unit_price = data[:, 1]
    discount = data[:, 2]

    return quantity, unit_price, discount


def numpy_calculation(quantity, unit_price, discount):
    revenue = quantity * unit_price * (1.0 - discount)

    total_revenue = np.sum(revenue)
    average_order_value = np.mean(revenue)
    large_sales_count = np.count_nonzero(revenue >= 5000)

    return {
        "total_revenue": float(total_revenue),
        "average_order_value": float(average_order_value),
        "large_sales_count": int(large_sales_count),
    }


def run_numpy_benchmark():
    # Сначала загружаем данные один раз.
    started = time.perf_counter()
    quantity, unit_price, discount = load_numpy_data()
    fetch_time = time.perf_counter() - started

    numpy_times = []
    result = None

    # Прогрев.
    result = numpy_calculation(quantity, unit_price, discount)

    for _ in range(REPEATS):
        started = time.perf_counter()
        result = numpy_calculation(quantity, unit_price, discount)
        elapsed = time.perf_counter() - started
        numpy_times.append(elapsed)

    # Отдельно измеряем полный путь:
    # PostgreSQL -> Python -> NumPy -> result.
    end_to_end_times = []

    for _ in range(REPEATS):
        started = time.perf_counter()
        q, p, d = load_numpy_data()
        result = numpy_calculation(q, p, d)
        elapsed = time.perf_counter() - started
        end_to_end_times.append(elapsed)

    return (
        result,
        fetch_time,
        numpy_times,
        end_to_end_times,
    )


def run_explain_analyze():
    explain_query = """
    EXPLAIN (ANALYZE, BUFFERS, FORMAT JSON)
    SELECT
        SUM(quantity * unit_price * (1 - discount)) AS total_revenue,
        AVG(quantity * unit_price * (1 - discount)) AS average_order_value,
        COUNT(*) FILTER (
            WHERE quantity * unit_price * (1 - discount) >= 5000
        ) AS large_sales_count
    FROM sales;
    """

    with psycopg.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cur:
            cur.execute(explain_query)
            plan = cur.fetchone()[0]

    # psycopg возвращает JSON как Python object для FORMAT JSON.
    if isinstance(plan, list):
        plan = plan[0]

    execution_time_ms = plan["Execution Time"]
    planning_time_ms = plan["Planning Time"]

    return planning_time_ms / 1000, execution_time_ms / 1000


def assert_results(sql_result, numpy_result):
    """
    Из-за различий numeric/float допускаем небольшую погрешность
    для сумм и среднего.
    """
    if not np.isclose(
        sql_result["total_revenue"],
        numpy_result["total_revenue"],
        rtol=1e-10,
        atol=0.01,
    ):
        raise AssertionError(
            f"total_revenue отличается:\n"
            f"SQL={sql_result['total_revenue']}\n"
            f"NumPy={numpy_result['total_revenue']}"
        )

    if not np.isclose(
        sql_result["average_order_value"],
        numpy_result["average_order_value"],
        rtol=1e-10,
        atol=1e-8,
    ):
        raise AssertionError(
            f"average_order_value отличается:\n"
            f"SQL={sql_result['average_order_value']}\n"
            f"NumPy={numpy_result['average_order_value']}"
        )

    if (
        sql_result["large_sales_count"]
        != numpy_result["large_sales_count"]
    ):
        raise AssertionError(
            f"large_sales_count отличается:\n"
            f"SQL={sql_result['large_sales_count']}\n"
            f"NumPy={numpy_result['large_sales_count']}"
        )


def main():
    print("PostgreSQL vs NumPy benchmark")
    print("=" * 35)

    with psycopg.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT COUNT(*) FROM sales")
            row_count = cur.fetchone()[0]

    print(f"Rows in PostgreSQL: {row_count:,}")

    print("\n1. PostgreSQL SQL")
    sql_result, sql_times = run_sql_benchmark()
    print_stats("SQL end-to-end", sql_times)

    planning_time, execution_time = run_explain_analyze()

    print(
        f"\nPostgreSQL EXPLAIN ANALYZE:"
        f"\nplanning:  {planning_time:.4f} s"
        f"\nexecution: {execution_time:.4f} s"
    )

    print("\n2. NumPy")
    (
        numpy_result,
        fetch_time,
        numpy_times,
        numpy_end_to_end_times,
    ) = run_numpy_benchmark()

    print(f"\nInitial PostgreSQL -> NumPy load: {fetch_time:.4f} s")
    print_stats("Pure NumPy calculation", numpy_times)
    print_stats(
        "PostgreSQL -> Python -> NumPy end-to-end",
        numpy_end_to_end_times,
    )

    assert_results(sql_result, numpy_result)

    print("\nResults are equal.")
    print("-" * 35)
    print(f"total_revenue:       {sql_result['total_revenue']:.2f}")
    print(f"average_order_value: {sql_result['average_order_value']:.6f}")
    print(f"large_sales_count:   {sql_result['large_sales_count']}")

    print("\nInterpretation")
    print("-" * 35)
    print(
        "SQL processes the data where it is stored: inside PostgreSQL."
    )
    print(
        "NumPy requires transferring the selected data from PostgreSQL "
        "to Python before calculation."
    )
    print(
        "Therefore compare both pure calculation time and "
        "end-to-end time. For real data engineering, the second "
        "comparison is often more representative."
    )


if __name__ == "__main__":
    main()
