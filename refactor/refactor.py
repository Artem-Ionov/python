"""Модуль, где был произведён рефакторинг"""

import datetime
from datetime import date

from bs4 import BeautifulSoup


def validate_link(href: str) -> bool:                       # Новая функция
    """Проверяем валидность ссылки"""                       # Более лаконично (устранили if)
    return "/upload/reports/oil_xls/oil_xls_" in href and href.endswith(".xls")


def get_date(href: str) -> date:                            # Новая функция
    """Извлекаем из ссылки дату в формате строки и преобразуем в объект datetime"""

    try:                                                    # Вынесли try/except в функцию
        date_str = href.split("oil_xls_")[1][:8]            # Более содержательные имена
        date_convert = datetime.datetime.strptime(date_str, "%Y%m%d").date()
        return date_convert
    except Exception as e:                                  # TODO: слишком общее исключение
        print(f"Не удалось извлечь дату из ссылки {href}: {e}")
        return None


def parse_page_links(html: str, start_date: date, end_date: date):  # Убрали неиспользуемый параметр url
    """
    Парсит ссылки на бюллетени с одной страницы. Пример ссылки:
    <a class="accordeon-inner__item-title link xls" href="/upload/reports/oil_xls/oil_xls_20240101_test.xls">link1</a>
    """

    results = []
    soup = BeautifulSoup(html, "html.parser")
    links = soup.find_all("a", class_="accordeon-inner__item-title link xls")

    for link in links:
        href = link.get("href")
        if not href:
            continue

        href = href.split("?")[0]
        if not validate_link(href):
            continue

        date_convert = get_date(href)
        if not date_convert:
            continue                                            # Добавили

        if start_date <= date_convert <= end_date:              # Переименовали u в url
            url = href if href.startswith("http") else f"https://spimex.com{href}"
            results.append((url, date_convert))
        else:
            print(f"Ссылка {href} вне диапазона дат")

    return results
