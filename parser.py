import requests
from bs4 import BeautifulSoup
import time
import random
import csv
from tabulate import tabulate

USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 16_2 like Mac OS X) AppleWebKit/537.36 (KHTML, like Gecko) Version/16.2 Mobile/15E148 Safari/537.36",
]


def get_page(url, max_retries=5):
    """Получает HTML страницы с учётом блокировок."""
    for attempt in range(max_retries):
        headers = {"User-Agent": random.choice(USER_AGENTS)}
        try:
            response = requests.get(url, headers=headers, timeout=10)
            if response.status_code == 200:
                return response.text
            elif response.status_code in [429, 503]:
                wait_time = random.uniform(5, 15)
                print(f"[*] Блокировка! Жду {wait_time:.2f} секунд...")
                time.sleep(wait_time)
        except requests.RequestException as e:
            print(f"[!] Ошибка: {e}")
    return None


def parse_labirint(url, limit=20):
    """Парсит книги с Labirint.ru (название, автор, цена)."""
    html = get_page(url)
    if not html:
        print("[!] Не удалось загрузить страницу.")
        return []

    soup = BeautifulSoup(html, "html.parser")
    books_data = []
    books = soup.find_all("div", class_="product-padding", limit=limit)

    for book in books:
        title_tag = book.find("a", class_="product-title-link")
        title = title_tag.get_text(strip=True) if title_tag else "Без названия"

        author_tag = book.find("div", class_="product-author")
        author = author_tag.get_text(strip=True) if author_tag else "Не указан"

        price_tag = book.find("span", class_="price-val")
        price = price_tag.get_text(strip=True) if price_tag else "Нет цены"

        books_data.append([title, author, price])

    return books_data


def save_to_csv(data, filename="books_data.csv"):
    """Сохраняет данные в CSV-файл."""
    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Название", "Автор", "Цена"])
        writer.writerows(data)
    print(f"[+] Данные сохранены в {filename}")


def main():
    """Основная функция для запуска парсера."""
    print("Добро пожаловать в парсер сайтов!")
    print("1. Labirint.ru (книги)")
    choice = input("Введите номер или URL: ").strip()

    if choice == "1":
        url = "https://www.labirint.ru/books/?tags=5542"
    else:
        url = choice

    try:
        limit = int(input("Сколько книг парсить (по умолчанию 20): ") or 20)
    except ValueError:
        limit = 20

    print(f"[*] Парсим {limit} книг с {url}...")
    data = parse_labirint(url, limit)

    if data:
        print(tabulate(data, headers=["Название", "Автор", "Цена"], tablefmt="grid"))
        save_to_csv(data)
    else:
        print("[!] Ничего не найдено.")


if name == "__main__":
    main()