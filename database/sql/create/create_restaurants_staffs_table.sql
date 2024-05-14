CREATE TABLE restaurants_staffs (
    staff_id VARCHAR(50) PRIMARY KEY,
    user_id VARCHAR(50) NOT NULL,
    restaurant_id VARCHAR(50) NOT NULL,
    role VARCHAR(100),
    FOREIGN KEY (user_id) REFERENCES users(user_id),
    FOREIGN KEY (restaurant_id) REFERENCES restaurants(restaurant_id)
);
