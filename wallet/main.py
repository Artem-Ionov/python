"""Главный файл программы, созданный для проверки правильности работы"""

from money import Money, Wallet
from currency import Currency

money1 = Money(500, Currency.RUB)
money2 = Money(300, Currency.RUB)
print(money1 + money2)                  # Проверяем __add__, а также __str__
print(money1 - money2)                  # __sub__

wallet = Wallet(balance={
    Currency.RUB: 400.0, 
    Currency.USD: 100.0, 
    })
print(wallet)                           # __str__
money3 = Money(200, Currency.EUR)
wallet.deposit(money3)                  # Методы класса Wallet
print(wallet)
wallet.remove(money2)
print(wallet)

print(wallet[Currency.USD])             # __getitem__
wallet[Currency.EUR] = 500.0            # __setitem__
print(wallet)
del wallet[Currency.RUB]                # __delitem__
print(wallet)
print(Currency.USD in wallet)           # __contain__
print(len(wallet))                      # __len__
