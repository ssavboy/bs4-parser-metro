# Parser metro

Небольшой консольный парсер категорий магазина **Метро**, написанный на Python с использованием библиотеки BeautifulSoup. Скрипт получает данные по выбранной категории и выводит их в консоль или сохраняет в CSV‑файл.

## Возможности

Основной режим работы парсера (`mode`):

- `coffee` — парсинг категории кофе на сайте Метро (название, цена и другие данные — по текущей реализации).

Опциональные параметры (`option`):

- `-h, --help` — вывод справки по аргументам для запуска парсера.
- `-c, --clear-cache` — очистка кэша запросов.
- `-o {pretty,file}, --output {pretty,file}` — формат вывода: табличный вывод через PrettyTable или сохранение в CSV‑файл.

Результаты парсинга сохраняются в директорию `parser/results` при выборе вывода в файл.

## Технологии

В проекте используются:

- `Python 3.x`  
- `beautifulsoup4` — парсинг HTML  
- `requests` / кэш запросов (если настроено)  
- `prettytable` — табличный вывод в терминал  
- `csv` — сохранение результатов в файл  

## Установка и запуск

1. Клонировать репозиторий:

   ```bash
   git clone https://github.com/ssavboy/bs4-parser-metro.git
   cd bs4-parser-metro
   ```

2. Создать и активировать виртуальное окружение:

   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # Linux/macOS
   source venv/bin/activate
   ```

3. Установить зависимости:

   ```bash
   pip install -r requirements.txt
   ```

4. Запуск парсера:

   ```bash
   python main.py coffee
   ```

5. Примеры с опциями:

   - Красивый вывод в консоль:

     ```bash
     python main.py coffee -o pretty
     ```

   - Сохранение результатов в CSV‑файл:

     ```bash
     python main.py coffee -o file
     ```

   - Очистка кэша перед запуском:

     ```bash
     python main.py coffee -c
     ```

## Структура проекта

- `parser/` — основная логика парсера и директория `results` для сохранения CSV‑файлов.
- `requirements.txt` — список зависимостей.
- `README.md` — документация по проекту.  
- `LICENSE` — лицензия MIT.

