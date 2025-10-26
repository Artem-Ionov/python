"""Модуль, где применяются различные скидки к заказу в зависимости от параметров заказа.
Выполним эту задачу с помощью паттерна 'стратегия' и частично 'фабрика'"""

from abc import ABC, abstractmethod


class Discount(ABC):
    """Абстрактный базовый класс для всех скидок.
    (Общий интерфейс для всех стратегий)"""

    @abstractmethod
    def apply(self, order: "Order") -> float:
        """Применение скидки к заказу"""

    @abstractmethod
    def is_applicable(self, order: "Order") -> bool:
        """Определение актуальности скидки для данного заказа"""


class ConstantDiscount(Discount):
    """Скидка на фиксированную сумму"""

    def apply(self, order: "Order") -> float:
        return order.price - 100

    def is_applicable(self, order: "Order") -> bool:
        return order.price < 1000


class PercentDiscount(Discount):
    """Скидка на процент от суммы заказа"""

    def apply(self, order: "Order") -> float:
        return order.price - order.price * 0.2

    def is_applicable(self, order: "Order") -> bool:
        return order.price > 2000


class RegularBuyerDiscount(Discount):
    """Скидка для постоянных покупателей"""

    def apply(self, order: "Order") -> float:
        return order.price - order.price * 0.1

    def is_applicable(self, order: "Order") -> bool:
        return order.regular_buyer


class Order:
    """Заказ (контекст)"""

    def __init__(self, price: float, regular_buyer: bool):
        """Параметры заказа"""

        self.price = price
        self.regular_buyer = regular_buyer
        self.discounts = [ConstantDiscount(), PercentDiscount(), RegularBuyerDiscount()]
        self.applicable_discounts = []

    def set_discounts(self):
        """Выбор скидок, применимых к конкретному заказу"""

        for discount in self.discounts:
            if discount.is_applicable(self):            # Передаю экземпляр текущего класса в метод другого класса
                self.applicable_discounts.append(discount)

    def process_order(self):
        """Применение всех актуальных скидок к заказу"""

        for discount in self.applicable_discounts:
            new_price = discount.apply(self)
            self.price = new_price                      # Накопление результатов


if __name__ == "__main__":

    order_1 = Order(price=3000, regular_buyer=True)
    order_1.set_discounts()
    order_1.process_order()
    print(order_1.price)
