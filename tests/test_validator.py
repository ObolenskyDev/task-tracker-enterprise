import sys
import os
import pytest

# Хак для настройки путей импорта (чтобы видеть папку src)
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.validator import TaskValidator

class TestTaskValidator:
    """
    Unit-тесты для проверки валидатора задач.
    Запускаются автоматически через GitHub Actions.
    """

    def test_valid_task(self):
        """Позитивный тест: Корректная задача должна проходить валидацию"""
        validator = TaskValidator()
        task = {"title": "Изучить Python", "priority": "high"}
        
        is_valid, msg = validator.validate(task)
        assert is_valid is True
        assert msg == "OK"

    def test_empty_title(self):
        """Негативный тест: Задача без заголовка должна отклоняться"""
        validator = TaskValidator()
        task = {"priority": "low"}
        
        is_valid, msg = validator.validate(task)
        assert is_valid is False
        assert "Не указан заголовок" in msg

    def test_invalid_priority(self):
        """Негативный тест: Неизвестный приоритет должен вызывать ошибку"""
        validator = TaskValidator()
        task = {"title": "Test", "priority": "super-high"}
        
        is_valid, msg = validator.validate(task)
        assert is_valid is False
        assert "Неверный приоритет" in msg
