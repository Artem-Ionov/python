"""Модуль, где поля модели описываются с помощью дескрипторов.
Это даёт синхонизацию полей модели с ключами словаря. При обращении к полю получаем значение
соответствующего ключа, при записи в поле - меняем значение соответствующего ключа."""

from typing import Any, TypeAlias

JSON: TypeAlias = dict[str, Any]                        # Псевдоним типа


class Field:
    """Класс-дескриптор"""

    def __init__(self, key: str):
        self.key = key                                  # Ключ словаря payload

    def __get__(self, instance: "Model", owner: type["Model"]):
        """Вызывается при обращении к атрибуту экземпляра (полю модели)"""
        if owner and instance is None:                  # Случай обращения по имени класса
            print("Обратись по имени экземпляра")
            return
        return instance.payload[self.key]               # Возращаем значение ключа из словаря payload

    def __set__(self, instance: "Model", value: Any):
        """Вызывается при присвоении значения атрибуту экземпляра (полю модели)"""
        instance.payload[self.key] = value              # Меняем значение ключа из словаря payload


class Model:
    """Модель работников фирмы"""

    def __init__(self, payload: JSON):
        self.payload = payload

    name = Field("name")
    age = Field("age")
    job = Field("job")


if __name__ == "__main__":

    payload = {"name": "Mike", "age": 30, "job": "engeneer"}

    model = Model(payload)
    print(model.name)                                   # Вызывается __get__
    print(model.age)
    print(model.job)

    Model.age                                           # __get__

    model.name = "Bob"                                  # __set__
    model.age = 45
    print(payload)                                      # Словарь изменился
