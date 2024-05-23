CREATE TABLE orders_items (
    orders_items_id SERIAL PRIMARY KEY,
    order_id INT NOT NULL,
    item_id VARCHAR(50) NOT NULL,
    quantity INT DEFAULT 1 CHECK (quantity > 0),
    price DECIMAL(10, 2) CHECK (price >= 0),
    FOREIGN KEY (order_id) REFERENCES orders(order_id),
    FOREIGN KEY (item_id) REFERENCES menus_items(item_id)
);
