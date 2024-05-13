CREATE TABLE restaurants_stand (
    stand_id VARCHAR(50) PRIMARY KEY,
    restaurant_id VARCHAR(50),
    name VARCHAR(255) NOT NULL,
    type VARCHAR(100),
    address TEXT,
    phone VARCHAR(20),
    campus_building VARCHAR(50),
    canteen_number VARCHAR(50),
    floor VARCHAR(25),
    meal_types TEXT[],
    operating_hours VARCHAR(50),
    campus VARCHAR(100),
    FOREIGN KEY (restaurant_id) REFERENCES restaurants(restaurant_id)
);
