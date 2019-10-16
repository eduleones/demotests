SHELL := /bin/bash

DJANGO_CMD = python demotests/manage.py

SETTINGS = demotests.settings

clean:
	@find . -name "*.pyc" | xargs rm -rf
	@find . -name "*.pyo" | xargs rm -rf
	@find . -name "__pycache__" -type d | xargs rm -rf
	@find . -name ".cache" -type d | xargs rm -rf

conf-env:
	@cp -n contrib/localenv .env
	@echo 'Please configure params from .env file.'
	@read continue


migrations:
	$(DJANGO_CMD) makemigrations $(app)

migrate:
	$(DJANGO_CMD) migrate

requirements-pip:
	@pip install --upgrade pip
	@pip install -r requirements/development.txt

requirements-apt:
	@echo 'Root access required to install system dependencies from `linux.apt` file'
	@sudo apt-get install $(shell cat requirements/linux.apt | tr "\n" " ")


# Installation

createsuperuser:
	$(DJANGO_CMD) createsuperuser

install-backend-linux: requirements-apt requirements-pip migrate
	@echo "[OK] Backend dependencies installed"

install_os_packages: conf-env install-backend-linux
	@echo "[OK] Installation completed"

create_token:
	$(DJANGO_CMD) drf_create_token $(user)

# Tests

test: SHELL:=/bin/bash
test: clean
	py.test demotests/ --ds=$(SETTINGS) -s

test-matching: SHELL:=/bin/bash
test-matching: clean
	py.test demotests/ -k $(test) --ds=$(SETTINGS) -s

coverage: clean
	coverage run --source='.' \
	demotests/manage.py test --noinput && \
	coverage report -m --skip-covered

# Lint and Style

lint: clean  ## Run the pylint test 
	@pylint -r y --rcfile=.pylintrc $(PROJECT_NAME)/*

isort: ## Run isort
	@isort -m 3 -tc

style:	## Run black auto formatting code style in the project
	@black -S -t py37 -l 80 $(PROJECT_NAME)/.

style-check:	## Run black check code style
	@black -S -t py37 -l 80 --check $(PROJECT_NAME)/.

# Development

shell: clean
	$(DJANGO_CMD) shell

runserver: clean
	$(DJANGO_CMD) runserver 0.0.0.0:8000

runserver-dev:
	set -a && source .env && set +a && $(DJANGO_CMD) runserver 0.0.0.0:$$APP_PORT

collectstatic: clean
	$(DJANGO_CMD) collectstatic

# Docker

docker-dev-up: clean ## Up docker-compose for development
	@docker-compose up -d

docker-dev-stop: clean ## Stop docker-compose for development
	@docker-compose stop