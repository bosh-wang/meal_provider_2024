CREATE TABLE menus_items (
    item_id VARCHAR(50) PRIMARY KEY,
    menu_id VARCHAR(50) NOT NULL,
    restaurant_id VARCHAR(50) NOT NULL,
    category VARCHAR(255) NOT NULL,
    item_name VARCHAR(255) NOT NULL,
    description TEXT,
    price INT NOT NULL,
    availability BOOLEAN DEFAULT TRUE,
    image BYTEA,  -- This column is for storing the binary data of the image
    image_url VARCHAR(255),  -- This column is for storing the URL to the image
    created_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (menu_id) REFERENCES menus(menu_id),
    FOREIGN KEY (restaurant_id) REFERENCES restaurants(restaurant_id)  -- Assuming 'restaurant_id' is the primary key in 'restaurants'
);

