# KoticBack — Мини бэкенд на Django & Django REST Framework

Простой и готовый к запуску бэкенд на Python / Django с REST API, упакованный в Docker.

---

## 🚀 Быстрый запуск через Docker

### 1. Сборка и запуск контейнера

```bash
docker build -t koticback .
docker run -p 8000:8000 koticback
```

Или с помощью **Docker Compose**:
```bash
docker compose up --build
```

После запуска сервис будет доступен по адресу: **http://localhost:8000**

---

## 🛠 Запуск локально (без Docker)

```bash
# 1. Создание и активация виртуального окружения
python3 -m venv venv
source venv/bin/activate  # На Windows: venv\Scripts\activate

# 2. Установка зависимостей
pip install -r requirements.txt

# 3. Применение миграций
python manage.py migrate

# 4. Запуск сервера разработки
python manage.py runserver 0.0.0.0:8000
```

---

## 📡 Доступные API эндпоинты

### 1. Healthcheck (проверка состояния сервиса)
- **URL**: `GET /api/health/`
- **Пример ответа**:
  ```json
  {
    "status": "ok",
    "service": "koticback",
    "cats_count": 0
  }
  ```

### 2. Управление котиками (CRUD API)
- **`GET /api/cats/`** — список всех котиков (с пагинацией и веб-интерфейсом DRF)
- **`POST /api/cats/`** — добавить нового котика
  ```bash
  curl -X POST http://localhost:8000/api/cats/ \
       -H "Content-Type: application/json" \
       -d '{"name": "Барсик", "breed": "Британский", "age": 3, "is_cute": true}'
  ```
- **`GET /api/cats/<id>/`** — получить информацию о конкретном котике
- **`PUT/PATCH /api/cats/<id>/`** — обновить данные котика
- **`DELETE /api/cats/<id>/`** — удалить котика
- **`GET /api/cats/random/`** — получить случайного котика из базы

---

## 🧪 Запуск тестов

```bash
python manage.py test
```

---

## 📂 Структура проекта

```text
koticback/
├── Dockerfile              # Инструкция сборки Docker-образа
├── .dockerignore           # Исключения для сборки Docker
├── docker-compose.yml      # Быстрый запуск через docker compose
├── requirements.txt        # Зависимости Python (Django, DRF, Gunicorn)
├── manage.py               # Утилита управления Django
├── config/                 # Настройки проекта
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
└── api/                    # Приложение API
    ├── models.py           # Модель Cat
    ├── serializers.py      # Сериализатор CatSerializer
    ├── views.py            # APIView и ModelViewSet
    ├── urls.py             # Маршрутизация эндпоинтов
    ├── admin.py            # Регистрация в панели администратора
    └── tests.py            # Тесты API
```
