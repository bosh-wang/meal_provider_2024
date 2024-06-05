CREATE TABLE employee_credits (
    credit_id SERIAL PRIMARY KEY,
    user_id INT NOT NULL,
    credit_limit DECIMAL(10, 2),
    current_due DECIMAL(10, 2),
    FOREIGN KEY (user_id) REFERENCES Users(user_id)
);
