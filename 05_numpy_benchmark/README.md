# PostgreSQL vs NumPy benchmark

Учебный стенд для второй недели курса «Python для анализа данных и инженерии данных».

## Структура

```text
pandas_numpy_sql_benchmark/
├── docker-compose.yaml
├── benchmark.py
└── init/
    └── 01_create_dataset.sql
```

## 1. Запуск PostgreSQL

```bash
docker compose up -d
```

PostgreSQL будет доступен на:

```text
localhost:5428
```

Проверка:

```bash
docker compose ps
```

Проверить количество строк:

```bash
docker exec -it pandas_numpy_sql_benchmark   psql -U benchmark -d benchmark   -c "SELECT COUNT(*) FROM sales;"
```

Ожидается:

```text
2500000
```

## 2. Установка Python-зависимостей

```bash
pip install numpy pandas psycopg[binary]
```

`pandas` здесь не обязателен для benchmark, но я оставил его в окружении,
потому что стенд предназначен для курса по Python/Pandas.

## 3. Запуск benchmark

```bash
python benchmark.py
```

Программа сравнивает один и тот же расчёт:

```text
revenue = quantity × unit_price × (1 - discount)
```

и получает три метрики:

- общая выручка;
- средний чек;
- количество продаж от 5000 рублей.

### SQL

PostgreSQL выполняет:

```sql
SELECT
    SUM(quantity * unit_price * (1 - discount)),
    AVG(quantity * unit_price * (1 - discount)),
    COUNT(*) FILTER (
        WHERE quantity * unit_price * (1 - discount) >= 5000
    )
FROM sales;
```

### NumPy

Python получает из PostgreSQL:

```text
quantity
unit_price
discount
```

и выполняет:

```python
revenue = quantity * unit_price * (1 - discount)
```

Затем:

```python
np.sum(revenue)
np.mean(revenue)
np.count_nonzero(revenue >= 5000)
```

## Важный педагогический момент

Нельзя просто сравнить:

```text
время SQL
vs
время NumPy
```

и объявить победителя.

Есть минимум три разных величины:

```text
1. SQL execution
   время вычисления внутри PostgreSQL

2. Pure NumPy
   время вычислений после загрузки данных в память

3. NumPy end-to-end
   PostgreSQL
       ↓
   передача данных
       ↓
   Python
       ↓
   NumPy
       ↓
   результат
```

Для Data Analyst/Data Engineer особенно интересен третий вариант.

## Почему таблица сделана широкой

В таблице есть не только три вычисляемых поля, но и дополнительные данные:

- category
- region
- payment_type
- comment
- customer_id
- product_id
- timestamp

Это делает dataset похожим на реальную таблицу фактов, а не на искусственный набор из трёх чисел.

Индексы намеренно не создаются: мы хотим сравнить массовое последовательное чтение и вычисление, а не точечный поиск по индексу.

## Если нужно пересоздать dataset

Важно: PostgreSQL init-скрипты выполняются только при первом создании volume.

Поэтому:

```bash
docker compose down -v
docker compose up -d
```

полностью удалит старый dataset и создаст его заново.

Команда `down -v` удаляет volume PostgreSQL — используйте её только если данные стенда больше не нужны.
