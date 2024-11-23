CREATE TABLE order_items (
    id INTEGER PRIMARY KEY,
    order_id INTEGER,
    price REAL,
    quantity INTEGER
);

INSERT INTO order_items (order_id, price, quantity) VALUES
(1, 10.0, 2),
(1, 15.0, 1),
(2, 20.0, 3);
