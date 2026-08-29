CREATE SCHEMA IF NOT EXISTS retail;
SET search_path TO retail;

CREATE TABLE customers (
    customer_id BIGINT PRIMARY KEY,
    first_name TEXT,
    city TEXT,
    segment TEXT,
    registration_date TIMESTAMP,
    email TEXT,
    acquisition_channel TEXT
);

CREATE TABLE products (
    product_id BIGINT PRIMARY KEY,
    product_name TEXT,
    category TEXT,
    subcategory TEXT,
    brand TEXT,
    list_price NUMERIC(14,2),
    price_tier TEXT
);

CREATE TABLE orders (
    order_id BIGINT PRIMARY KEY,
    customer_id BIGINT REFERENCES customers(customer_id),
    order_ts TIMESTAMP,
    status TEXT,
    channel TEXT,
    payment_method TEXT,
    delivery_city TEXT,
    updated_at TIMESTAMP
);

CREATE TABLE order_items (
    order_id BIGINT REFERENCES orders(order_id),
    product_id BIGINT REFERENCES products(product_id),
    quantity INTEGER,
    list_price NUMERIC(14,2),
    discount_pct NUMERIC(8,4),
    unit_price NUMERIC(14,2),
    revenue NUMERIC(16,2)
);

CREATE TABLE returns (
    return_id BIGINT PRIMARY KEY,
    order_id BIGINT,
    product_id BIGINT,
    return_ts TIMESTAMP,
    reason TEXT,
    refund_amount NUMERIC(16,2)
);

CREATE TABLE marketing_campaigns (
    campaign_id BIGINT PRIMARY KEY,
    campaign_name TEXT,
    channel TEXT,
    start_date DATE,
    end_date DATE,
    budget NUMERIC(16,2),
    target_segment TEXT
);

CREATE TABLE customer_events (
    event_id BIGINT PRIMARY KEY,
    event_ts TIMESTAMP,
    customer_id BIGINT,
    event_type TEXT,
    device TEXT,
    source TEXT,
    product_id BIGINT,
    session_id BIGINT
);

CREATE TABLE support_tickets (
    ticket_id BIGINT PRIMARY KEY,
    customer_id BIGINT,
    created_at TIMESTAMP,
    category TEXT,
    priority TEXT,
    status TEXT,
    resolution_hours NUMERIC(10,2)
);

CREATE TABLE inventory_snapshots (
    snapshot_date DATE,
    product_id BIGINT,
    stock_units INTEGER,
    reorder_point INTEGER
);
