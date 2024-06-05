CREATE TABLE Reminders (
    reminder_id SERIAL PRIMARY KEY,
    user_id INT NOT NULL,
    message TEXT,
    reminder_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES Users(user_id)
);
