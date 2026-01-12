-- 1. Сложный запрос: Сводная статистика по задачам для каждого пользователя
-- Показывает имя, общее кол-во задач и только те, что в работе
SELECT 
    u.username, 
    COUNT(t.task_id) AS total_tasks,
    SUM(CASE WHEN t.status = 'in_progress' THEN 1 ELSE 0 END) AS active_tasks
FROM users u
LEFT JOIN tasks t ON u.user_id = t.user_id
GROUP BY u.user_id, u.username
ORDER BY total_tasks DESC;

-- 2. Запрос на проверку целостности: Найти задачи, у которых некорректно привязан пользователь
SELECT * FROM tasks WHERE user_id NOT IN (SELECT user_id FROM users);
