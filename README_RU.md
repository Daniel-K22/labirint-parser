```markdown
 # Labirint Parser
 Парсер для сайта Labirint.ru, который собирает данные о книгах (название, автор, цена) и сохраняет их в CSV.

 ## Возможности
 - Парсинг книг с Labirint.ru с указанием количества.
 - Обход блокировок с помощью смены User-Agent и задержек.
 - Вывод данных в таблице и сохранение в CSV.
 
   ```
 ## Установка
 1. Склонируйте репозиторий:
```bash
    git clone https://github.com/Daniel-K22/labirint-parser.git

   ```
 2. Установите зависимости:
```bash
    pip install -r requirements.txt

   ```
 3. Запустите парсер:
```bash
    python parser.py

 ## Использование
 1. Запустите скрипт.
 2. Выберите сайт (1 для Labirint.ru или введите свой URL).
 3. Укажите, сколько книг парсить.
 4. Получите таблицу и файл books_data.csv.

  ```
## Технологии
 - Python  
 - Requests, BeautifulSoup4, Tabulate

 ## Автор
 Daniel-K22 — разработчик с опытом в парсинге и автоматизации.
 
