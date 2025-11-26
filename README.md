# Описание проекта

Этот проект реализует полноценный конвейер машинного обучения, включающий сбор данных, предобработку, обучение модели, инференс, мониторинг и деплой через Docker. Также предоставлен Makefile для удобной автоматизации рутинных задач.

---

## Структура проекта

```
project/
├── data_pipeline/
│   ├── collect_data.py        # сбор данных
│   ├── validate_data.py       # проверка качества сырых данных
│   └── preprocess_data.py     # подготовка данных
│
├── training/
│   ├── train_model.py         # переобучение модели
│   ├── evaluate_model.py      # вычисление метрик
│   └── save_model.py          # сохранение модели
│
├── inference/
│   ├── predict.py             # инференс
│   └── serve_api.py           # API FastAPI
│
├── monitoring/
│   ├── data_drift.py          # анализ дрейфа данных (PSI)
│   ├── model_drift.py         # анализ метрик модели
│   └── generate_report.py     # отчёты и графики
│
├── models/
│   ├── final_model.pkl        # сохранённая модель
│   ├── features.pkl           # список фичей
│   └── model_params.pkl       # параметры модели
│
├── Dockerfile                 # основной docker-файл
├── docker-compose.yaml        # docker-compose
├── requirements.txt           # зависимости
├── Makefile                   # автоматизация команд
└── README.md
```

---

## Запуск проекта

### 1. Клонирование репозитория

```
git clone https://github.com/Valrick1029/LightGBM_classification.git
cd project
```

### 2. Сборка и запуск контейнеров Docker

```
docker-compose up --build
```

### 3. Запуск API локально без Docker

```
uvicorn inference.serve_api:app --reload
```

---

## Команды Makefile

| Команда             | Описание                                 |
| ------------------- | ---------------------------------------- |
| `make train`        | запустить обучение модели                |
| `make evaluate`     | посчитать метрики                        |
| `make preprocess`   | выполнить очистку и подготовку данных    |
| `make infer`        | выполнить инференс для тестового примера |
| `make api`          | запустить FastAPI сервер                 |
| `make docker-build` | собрать Docker образ                     |
| `make docker-up`    | поднять сервисы через docker-compose     |

---

## Пример использования API

Запрос:

```json
{
  "risk_factor": 0.12,
  "first_tx_timestamp": 1680000000,
  "max_eth_ever": 2.5
}
```

Ответ:

```json
{
  "prediction": 1,
  "probability": 0.87
}
```

---

## Мониторинг

- **data\_drift.py** — PSI, распределения, дрейф данных
- **model\_drift.py** — сравнение текущих метрик с эталонными
- **generate\_report.py** — графики, отчеты

Все результаты сохраняются в `monitoring/reports`.

---

## Разработка

Установка зависимостей:

```
pip install -r requirements.txt
```

Форматирование кода:

```
black .
```

Проверка кода:

```
flake8
```

---

## Лицензия

MIT License

