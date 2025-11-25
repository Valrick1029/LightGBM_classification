# 1. Базовый образ — Python
FROM python:3.10-slim

# 2. Устанавливаем рабочую директорию
WORKDIR /app

# 3. Копируем файл зависимостей
COPY requirements.txt .

# 4. Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# 5. Копируем весь проект в контейнер
COPY . .

# 6. Указываем порт (опционально)
EXPOSE 8000

# 7. Команда запуска API (FastAPI через uvicorn)
CMD ["uvicorn", "inference.serve_api:app", "--host", "0.0.0.0", "--port", "8000"]
