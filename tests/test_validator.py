import sys
import os
import pytest

# Добавляем путь к папке src, чтобы тесты её видели
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.validator import TaskValidator

def test_valid_task():
    validator = TaskValidator()
    is_valid, msg = validator.validate({"title": "Test Task", "priority": "high"})
    assert is_valid is True

def test_empty_title():
    validator = TaskValidator()
    is_valid, msg = validator.validate({"priority": "low"})
    assert is_valid is False
    assert "Не указан заголовок" in msg