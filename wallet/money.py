"""Модуль для определения основных классов"""

from dataclasses import dataclass

from currency import Currency
from exceptions import NegativeValueException, NotComparisonException


@dataclass
class Money:
    """Представление денежной суммы в определённой валюте"""

    value: float
    currency: Currency

    def __post_init__(self):
        """Валидация параметров конструктора. Метод применяется с dataclass"""
        if self.value < 0:
            raise NegativeValueException("Денежная сумма не может быть отрицательна")

    def __add__(self, other: "Money") -> "Money":
        """Сложение двух денежных сумм"""
        if self.currency != other.currency:
            raise NotComparisonException("Валюты не совпадают")
        return Money(self.value + other.value, self.currency)

    def __sub__(self, other: "Money") -> "Money":
        """Вычетание двух денежных сумм"""
        if self.currency != other.currency:
            raise NotComparisonException("Валюты не совпадают")
        return Money(self.value - other.value, self.currency)

    def __str__(self):
        """Удобочитаемое представление денежной суммы"""
        return f"Денежная сумма: {self.value}, {self.currency.value}"       # Тут currency.value - атрибут Enum


@dataclass
class Wallet:
    """Кошелёк для хранения денег в различных валютах"""

    balance: dict[Currency, float]

    def __post_init__(self):
        """Валидация параметров конструктора. Метод применяется с dataclass"""
        for key in self.balance.keys():
            if self.balance[key] < 0:
                raise NegativeValueException(
                    f"Сумма по валюте {key.value} отрицательна"
                )

    def __str__(self):
        """Удобочитаемое представление кошелька"""
        balance_str = "В кошельке "
        for currency, value in self.balance.items():
            balance_str += f"{value} {currency.value}, "
        return balance_str

    def __getitem__(self, index: Currency):
        """Получение баланса определённой валюты"""
        return self.balance[index]

    def __setitem__(self, index: Currency, value: float):
        """Задание баланса определённой валюты"""
        self.balance[index] = value

    def __delitem__(self, index: Currency):
        """Удаление определённой валюты из кошелька"""
        self.balance.pop(index)

    def __contains__(self, currency: Currency):
        """Проверка наличия определённой валюты в кошельке"""
        return currency in self.balance

    def __len__(self):
        """Получение количества валют в кошельке"""
        return len(self.balance)

    def deposit(self, money: Money):
        """Пополнение кошелька"""
        current_balance = self.balance.get(money.currency, 0)               # На случай, если в кошельке нет такой валюты
        self.balance[money.currency] = current_balance + money.value

    def remove(self, money: Money):
        """Снятие денег с кошелька"""
        self.balance[money.currency] -= money.value
        if self.balance[money.currency] < 0:
            raise NegativeValueException("Сумма для снятия больше баланса")
