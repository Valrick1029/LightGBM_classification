# ==== Переменные ====
PYTHON=python3
VENV=.venv
PIP=$(VENV)/bin/pip
PY=$(VENV)/bin/python

# ==== Создание виртуального окружения ====

venv:
	@echo ">>> Создаю виртуальное окружение"
	python3 -m venv $(VENV)
	$(PIP) install --upgrade pip

install: venv
	@echo ">>> Устанавливаю зависимости"
	$(PIP) install -r requirements.txt

# ==== Работа с данными ====

collect_data:
	$(PY) data_pipeline/collect_data.py

validate_data:
	$(PY) data_pipeline/validate_data.py

preprocess_data:
	$(PY) data_pipeline/preprocess_data.py

# ==== Обучение ====

train:
	$(PY) training/train_model.py

evaluate:
	$(PY) training/evaluate_model.py

save_model:
	$(PY) training/save_model.py

# ==== Инференс ====

predict:
	$(PY) inference/predict.py

serve_api:
	$(PY) inference/serve_api.py

# ==== Мониторинг ====

data_drift:
	$(PY) monitoring/data_drift.py

model_drift:
	$(PY) monitoring/model_drift.py

monitoring_report:
	$(PY) monitoring/generate_report.py

# ==== Docker ====

docker_build:
	docker build -t ml_project .

docker_run:
	docker run -p 8000:8000 ml_project

docker_monitoring_build:
	docker build -f Dockerfile.monitoring -t ml_monitoring .

docker_monitoring_run:
	docker run ml_monitoring

# ==== Git ====

git_add:
	git add .

git_commit:
	git commit -m "update"

git_push:
	git push

# ==== Очистка ====

clean:
	rm -rf __pycache__ */__pycache__ .pytest_cache *.pkl *.log

clean_data:
	rm -rf data/raw/* data/processed/*

clean_all: clean clean_data
	rm -rf $(VENV)

