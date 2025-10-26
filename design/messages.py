"""Реализация паттерна 'фабрика' для системы обработки сообщений"""

from abc import ABC, abstractmethod
from typing import Any


class JsonMessage:
    """Исходное сообщение"""

    def __init__(self, message_type: str, payload: dict[str, Any]):
        self.message_type = message_type
        self.payload = payload


class ParsedMessage:
    """Унифицированное представление сообщения"""


class MessageParser(ABC):
    """Абстрактный базовый класс для всех парсеров"""

    @abstractmethod
    def process_message(self, message: JsonMessage) -> ParsedMessage:
        """Преобразует сообщение из определённого источника в унифицированный формат"""


class TelegramMessageParser(MessageParser):
    """Реализация парсера для сообщения из Telegram"""

    def process_message(self, message: JsonMessage) -> ParsedMessage:
        print("Telegram")


class SlackMessageParser(MessageParser):
    """Реализация парсера для сообщения из Slack"""

    def process_message(self, message: JsonMessage) -> ParsedMessage:
        print("Slack")


class MattermostMessageParser(MessageParser):
    """Реализация парсера для сообщения из Mattermost"""

    def process_message(self, message: JsonMessage) -> ParsedMessage:
        print("Mattermost")


class ParserFactory:
    """Фабрика парсеров
    Если информация о состоянии не требуется, можно заменить self.parsers
    на переменную и дополнить get_parsers @staticmethod или @classmethod"""

    def __init__(self):
        """Регистр парсеров"""

        self.parsers = {
            "telegram": TelegramMessageParser,
            "slack": SlackMessageParser,
            "mattermost": MattermostMessageParser,
        }

    def get_parser(self, message_type: str):
        """Возвращает обработчик парсеров в зависимости от типа сообщения"""
        if message_type not in self.parsers:
            raise ValueError("Неизвестный тип парсера")
        return self.parsers[message_type]()


if __name__ == "__main__":

    msg = JsonMessage("telegram", {"a": 1})
    fact = ParserFactory()
    parser = fact.get_parser(msg.message_type)          # Получаем парсер, соответствующий типу сообщения
    parser.process_message(msg)                         # Парсер выполняет обработку сообщения
