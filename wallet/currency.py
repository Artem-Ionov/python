"""Модуль для определения доступных валют"""

from enum import Enum

class Currency(Enum):
    """Задание поддерживаемых валют"""
    RUB = 'RUB'
    USD = 'USD'
    EUR = 'EUR'