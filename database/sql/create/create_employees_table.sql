CREATE TABLE employees (
    employee_id VARCHAR(255) PRIMARY KEY,
    user_id VARCHAR(50) NOT NULL,
    department VARCHAR(255),
    position VARCHAR(255),
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);
