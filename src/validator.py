class TaskValidator:
    def validate(self, task: dict):
        if not task or not isinstance(task, dict):
            return False, "Ошибка: Данные должны быть словарем"
        if not task.get('title'):
            return False, "Ошибка: Не указан заголовок задачи"
        
        valid_priorities = ['low', 'medium', 'high']
        priority = task.get('priority', 'low')
        
        if priority not in valid_priorities:
            return False, f"Ошибка: Неверный приоритет '{priority}'"
            
        return True, "OK"