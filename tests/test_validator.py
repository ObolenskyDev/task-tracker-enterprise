import pytest
from src.validator import TaskValidator

# 1. Позитивный тест (Happy Path)
def test_valid_task_creation():
    validator = TaskValidator()
    # Создаем правильную задачу
    task = {"title": "Изучить Python", "priority": "high"}
    
    is_valid, message = validator.validate(task)
    
    # Assert - это "ожидание". Если тут False, тест упадет красным
    assert is_valid is True
    assert message == "OK"

# 2. Негативный тест: Пустой заголовок
def test_missing_title():
    validator = TaskValidator()
    # Задача без названия
    task = {"priority": "low"}
    
    is_valid, message = validator.validate(task)
    
    assert is_valid is False
    assert message == "Ошибка: Не указан заголовок задачи"

# 3. Негативный тест: Неверный приоритет
def test_invalid_priority():
    validator = TaskValidator()
    # Приоритет "super-mega-high" не существует в системе
    task = {"title": "Test", "priority": "super-mega-high"}
    
    is_valid, message = validator.validate(task)
    
    assert is_valid is False
    assert "Неверный приоритет" in message