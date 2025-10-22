"""Модуль для определения кастомных исключений"""

class NegativeValueException(Exception):
    """Кастомное исключение отрицательного баланса"""
    pass

class NotComparisonException(Exception):
    """Кастомное исключение несовпадения валют"""
    pass

