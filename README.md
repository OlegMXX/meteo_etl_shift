# Meteo ETL

## Описание
**Meteo ETL** — это приложение для автоматизации сбора метеоданных с https://open-meteo.com/, их обработки и записи в базу данных или выгрузки в CSV-файл.
- **Язык разработки**: Python
- **База данных**: PostgreSQL 13
- **Прочие библиотеки**:
  - **asyncpg** — асинхронная работа с PostgreSQL.
  - **requests** — HTTP-запросы.
  - **passlib** — библиотека для работы с хэшированием паролей, включая поддержку bcrypt.
  - **pre-commit** — автоматическое выполнение линтеров и других проверок перед коммитами.
  - **python-dotenv** — работа с переменными окружения из файла `.env`.

## Запуск проекта

1. Создать виртуальное окружение

для Windows:

```
python -m venv venv
```
для Linux:

```
python3 -m venv venv
```

2. Активировать окружение

для Windows:

```
venv/Scripts/activate.ps1
```

для Linux:

```
source venv/bin/activate
```

3. Установить зависимости

```
pip install -r requirements.txt
```

4. В корневой директории проекта создать файл
.env для переменных окружение
файл заполнить следующими данными или использовать свои.

```
#=====POSTGRESS_SETTINGS=====#

POSTGRES_HOST=localhost
POSTGRES_PORT=5432
POSTGRES_USER=admin
POSTGRES_PASSWORD=admin
POSTGRES_DB=db


````


5. Запуск инстанса БД

```
docker-compose up --build
```

6. Запустить файл main.py

```
python src/main.py
````

7. Следуйте инструкциям приложения.

Пример ввода:
```
2025-05-01
2025-05-10
y
y
````
