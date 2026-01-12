class TaskValidator:
    """
    Класс валидации бизнес-логики задач.
    Используется перед сохранением задачи в Базу Данных.
    """

    def validate(self, task: dict):
        """
        Проверяет корректность полей задачи.
        
        Args:
            task (dict): Словарь с данными задачи (title, priority, etc.)
            
        Returns:
            tuple: (bool success, str message) - Результат проверки и сообщение.
        """

        # Проверка на тип данных
        if not task or not isinstance(task, dict):
            return False, "Ошибка: Данные должны быть словарем"

        # 1. Проверка обязательного поля 'title'
        if not task.get('title'):
            return False, "Ошибка: Не указан заголовок задачи"

        # 2. Проверка допустимых значений приоритета
        valid_priorities = ['low', 'medium', 'high']
        priority = task.get('priority', 'low') # low по умолчанию

        # ... код проверки приоритета ...
        if priority not in valid_priorities:
            return False, f"Ошибка: Неверный приоритет '{priority}'"

        # TODO: Добавить маппинг (конвертацию) приоритетов перед записью в БД:
        # 'low' -> 1, 'medium' -> 2, 'high' -> 3.
        # Сейчас база принимает INT, а мы валидируем STR.

        # Если все проверки пройдены
        return True, "OK"