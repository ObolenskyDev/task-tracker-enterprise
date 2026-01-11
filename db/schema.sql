-- Задача: SCRUM-2
-- Автор: [Твое Имя]
-- Описание: Схема базы данных для Task Tracker

CREATE DATABASE IF NOT EXISTS task_tracker;
USE task_tracker;

-- 1. Таблица пользователей (User Management)
CREATE TABLE users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    email VARCHAR(100) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 2. Таблица задач (Task Management)
CREATE TABLE tasks (
    task_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    title VARCHAR(200) NOT NULL,
    description TEXT,
    status ENUM('new', 'in_progress', 'done') DEFAULT 'new',
    priority INT DEFAULT 1,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
);

-- Примеры аналитических запросов (для команды):
-- SELECT * FROM tasks WHERE status = 'in_progress';