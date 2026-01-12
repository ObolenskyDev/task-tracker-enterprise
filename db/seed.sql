-- Наполнение пользователями
INSERT INTO users (username, email) VALUES 
('obolensky_n', 'nikita@example.com'),
('ivanov_i', 'ivan@example.com'),
('petrov_p', 'petr@example.com');

-- Наполнение задачами (разные статусы и приоритеты)
INSERT INTO tasks (user_id, title, description, status, priority) VALUES 
(1, 'Настроить CI/CD', 'Настройка GitHub Actions для тестов', 'in_progress', 3),
(1, 'Тесты API', 'Добавить коллекцию Postman в репозиторий', 'done', 2),
(2, 'Обновить документацию', 'Описать эндпоинты в README', 'new', 1),
(3, 'Фикс багов', 'Исправить валидацию email в форме регистрации', 'new', 3);