# RetailPulse — учебный проект курса

RetailPulse — синтетическая, но реалистичная модель интернет-магазина. Один бизнес-контекст сопровождает студента почти весь курс: от первых задач Pandas до финального ETL/Airflow pipeline.

## Основные бизнес-вопросы

- как меняется выручка;
- какие товары и категории самые успешные;
- кто лучшие и «уснувшие» клиенты;
- какие каналы привлечения эффективнее;
- где возникают возвраты;
- где теряются пользователи в воронке;
- как связаны продажи, поддержка и качество сервиса;
- как автоматизировать ежедневную загрузку данных.

## Таблицы

- `customers` — 10 000 клиентов;
- `products` — 250 товаров;
- `orders` — 60 000 заказов за 2025-01-01 — 2026-06-30;
- `order_items` — позиции заказов;
- `returns` — 7 000 возвратов;
- `customer_events` — 120 000 событий поведения;
- `marketing_campaigns` — 30 кампаний;
- `support_tickets` — 18 000 обращений;
- `inventory_snapshots` — еженедельные снимки остатков.

## По неделям

### Неделя 1
`customer_events_raw.csv`, `orders_raw.csv`
- генераторы;
- потоковая обработка;
- чтение большими частями;
- память.

### Неделя 2
`orders_clean.csv`, `order_items_clean.csv`
- vectorization;
- расчёт скидок и выручки;
- сравнение циклов и NumPy.

### Недели 3–7
`customers_raw.csv`, `products.csv`, `orders_raw.csv`, `order_items_raw.csv`, `returns.csv`, `customer_events_raw.csv`
- очистка;
- groupby;
- merge;
- временные показатели;
- возвраты;
- retention;
- воронка;
- бизнес-метрики.

### Неделя 8 — EDA
Кейс: **«Почему изменилась выручка интернет-магазина?»**
Студент формирует гипотезы сам и проверяет их по данным.

### Неделя 9 — PostgreSQL
JOIN, агрегаты, подзапросы, Python ↔ PostgreSQL.

### Неделя 10 — API
`03_api_mock_data`
- pagination;
- retries;
- checkpoint;
- incremental loading;
- дедупликация.

### Неделя 11 — ETL / ELT
API → raw → validation → transformation → PostgreSQL.

Требования:
- повторный запуск не создаёт дубликаты;
- ошибка одной страницы не уничтожает уже загруженные данные;
- pipeline умеет продолжить работу с checkpoint.

### Неделя 12 — Production Python
Оформить pipeline как проект с configuration, `.env`, modules, logging, type hints и Pydantic.

### Неделя 13 — Testing / Data Quality
Проверить:
- уникальность order_id;
- существование customer_id;
- quantity > 0;
- revenue >= 0;
- обязательные поля;
- корректность дат;
- допустимые значения статусов.

### Неделя 14 — большие данные
Исходные CSV → Parquet → DuckDB. Сравнить CSV/Parquet, Pandas/DuckDB и разные стратегии чтения.

### Неделя 15 — Airflow + Docker
Оркестрация полного pipeline: API → raw → quality → transform → PostgreSQL.

### Неделя 16 — финальный проект
«Постройте аналитическую платформу RetailPulse»: ingestion, raw, quality, transformations, PostgreSQL, витрины, Airflow, Docker, тесты и README.

## Намеренно заложенные проблемы качества

Raw-файлы содержат:
- пропуски;
- дубликаты;
- разный регистр email;
- пробелы в event_type;
- некорректные quantity;
- аномальные скидки;
- пропуски customer_id в событиях.

`*_raw.csv` — для очистки и Data Quality.
`*_clean.csv` — для задач, где можно сразу перейти к аналитике.
