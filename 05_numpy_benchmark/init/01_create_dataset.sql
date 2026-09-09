-- Большой тестовый dataset.
-- Цель: получить сотни мегабайт данных в PostgreSQL без отдельного CSV-файла.
--
-- Важно: скрипты из /docker-entrypoint-initdb.d выполняются только
-- при ПЕРВОМ создании пустого volume PostgreSQL.

CREATE TABLE sales (
    sale_id       BIGINT PRIMARY KEY,
    sale_ts       TIMESTAMP NOT NULL,
    customer_id   INTEGER NOT NULL,
    product_id    INTEGER NOT NULL,
    category      VARCHAR(40) NOT NULL,
    quantity      INTEGER NOT NULL,
    unit_price    NUMERIC(12, 2) NOT NULL,
    discount      NUMERIC(5, 4) NOT NULL,
    region        VARCHAR(30) NOT NULL,
    payment_type  VARCHAR(20) NOT NULL,
    comment       VARCHAR(120) NOT NULL
);

-- 2.5 млн строк. За счёт текстовых полей таблица получается
-- достаточно большой для заметного benchmark.
INSERT INTO sales (
    sale_id,
    sale_ts,
    customer_id,
    product_id,
    category,
    quantity,
    unit_price,
    discount,
    region,
    payment_type,
    comment
)
SELECT
    gs AS sale_id,
    TIMESTAMP '2024-01-01'
        + ((gs % 525600) * INTERVAL '1 minute') AS sale_ts,
    1 + (gs % 100000) AS customer_id,
    1 + ((gs * 17) % 50000) AS product_id,
    (ARRAY[
        'electronics',
        'home',
        'sport',
        'books',
        'beauty',
        'food',
        'clothes',
        'garden'
    ])[1 + (gs % 8)] AS category,
    1 + (gs % 10) AS quantity,
    ROUND((50 + ((gs * 37) % 200000) / 100.0)::numeric, 2) AS unit_price,
    ROUND(((gs % 31) / 100.0)::numeric, 4) AS discount,
    (ARRAY[
        'north',
        'south',
        'east',
        'west',
        'central'
    ])[1 + (gs % 5)] AS region,
    (ARRAY[
        'card',
        'cash',
        'transfer',
        'online'
    ])[1 + (gs % 4)] AS payment_type,
    'synthetic benchmark record #' || gs ||
        ' customer=' || (1 + (gs % 100000)) ||
        ' product=' || (1 + ((gs * 17) % 50000)) AS comment
FROM generate_series(1, 2500000) AS gs;

ANALYZE sales;

-- Не создаём индексы специально:
-- benchmark должен сравнивать обработку большого набора данных,
-- а не преимущество индекса при выборке нескольких строк.
