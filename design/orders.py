"""Модуль, где применяются различные скидки к заказу в зависимости от параметров заказа.
Выполним эту задачу с помощью паттерна 'стратегия' """

from abc import ABC, abstractmethod

class Discount(ABC):
    """Абстрактный базовый класс для всех скидок.
    (Общий интерфейс для всех стратегий)"""

    @abstractmethod
    def apply(self, order: int):
        """Применение скидки к заказу"""
        pass


class ConstantDiscount(Discount):
    """Скидка на фиксированную сумму"""

    def apply(self, price: int):
        return price - 100


class PercentDiscount(Discount):
    """Скидка на процент от суммы заказа"""

    def apply(self, price: int):
        return price - price * 0.2
    

class RegularBuyerDiscount(Discount):
    """Скидка для постоянных покупателей"""

    def apply(self, price: int):
        return price - price * 0.1
    

class Order:
    """Заказ"""

    def __init__(self, price: float, regular_buyer: bool):
        """Параметры заказа"""

        self.price = price
        self.regular_buyer = regular_buyer
        self.discount = None

    def set_discount(self, discount):
        self.discount = discount

    def process_order(self):
        return self.discount.apply(self.price)


if __name__ == "__main__":
    
    order_1 = Order(price=10000, regular_buyer=True)
    order_1.set_discount(ConstantDiscount())
    print(order_1.process_order())