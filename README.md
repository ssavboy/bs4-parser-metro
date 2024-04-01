# парсинг категорий Метро

## Описание аргументов и параметров

Режимы работы парсера `mode`:
  * `coffee` - парсинг катерогии кофе

Опциональные параметры `option`:
  * `-h, --help` - описание аргументов для запуска парсера
  * `-c, --clear-cache` - очистка кэша
  * `-o {pretty,file}, --output {pretty,file}` - способы вывода информации, `PrettyTable` | `csv-файл`


## Подготовка и запуск проекта

- Создать и активировать виртуальное окружение
    ```
    python -m venv venv
    ```
- Установить зависимости
    ```
    pip install -r requirements.txt
    ```
- Запустить main.py
    ```
    python main.py <mode> [option]

- csv файл в parser/results