CREATE TABLE orders (
    order_id SERIAL PRIMARY KEY,
    user_id VARCHAR(50) NOT NULL,
    restaurant_id VARCHAR(50) NOT NULL,
    order_status VARCHAR(100) DEFAULT 'PENDING',
    total_price DECIMAL(10, 2),
    order_date TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
    confirmed_date TIMESTAMPTZ,  -- 餐廳確認訂單時間
    prepared_date TIMESTAMPTZ,   -- 餐廳完成準備時間
    completed_date TIMESTAMPTZ,  -- 客戶完成取餐時間
    canceled_date TIMESTAMPTZ,   -- 訂單取消時間
    paid BOOLEAN DEFAULT FALSE,
    FOREIGN KEY (user_id) REFERENCES users(user_id),
    FOREIGN KEY (restaurant_id) REFERENCES restaurants(restaurant_id)
);
