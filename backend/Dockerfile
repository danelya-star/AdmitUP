# 1. Базовый образ
FROM python:3.11-slim

# 2. Установка рабочей директории
WORKDIR /app

# 3. Установка зависимостей
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Копирование кода приложения
COPY ./app ./app

# 5. Указание порта
EXPOSE 8000

# 6. Команда для запуска
# Запускаем uvicorn, чтобы он был доступен извне контейнера.
# В продакшене секреты (MONGO_URL, OPENAI_API_KEY, JWT_SECRET)
# должны передаваться через переменные окружения платформы деплоя.
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]