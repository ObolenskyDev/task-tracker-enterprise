class TaskValidator:
    """
    Класс для проверки корректности данных задачи перед сохранением.
    """

    def validate(self, task: dict):
        """
        Проверяет словарь задачи.
        Возвращает: (успех: bool, ошибка: str)
        """
        
        # 1. Проверка: Заголовок обязателен
        if not task.get('title'):
            return False, "Ошибка: Не указан заголовок задачи"

        # 2. Проверка: Приоритет должен быть корректным
        valid_priorities = ['low', 'medium', 'high']
        priority = task.get('priority', 'low') # Если не указан, считаем low
        
        if priority not in valid_priorities:
            return False, f"Ошибка: Неверный приоритет '{priority}'"

        # 3. Успех: Все проверки пройдены
        return True, "OK"