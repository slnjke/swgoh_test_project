DIRS_TO_CLEAN =   .cache \
	 build \
	 .pytest_cache \
	 __pycache__ \
	 .mypy_cache \
	 logs \
	 .venv \
	 ./allure-* \
	.env \
	.overseer \
	.local \
	.bash_history \

ifeq (, $(shell which docker-compose))
COMPOSE ?= docker compose --progress plain
else
COMPOSE ?= docker-compose
endif


venv:
	uv venv --clear
	uv sync --no-dev

venv_dev:
	uv venv --clear
	uv sync

install_dev: .env dirs	venv_dev install_pre_commit docker-build up

install: .env dirs	venv  docker-build up

docker-build: .env
	docker-compose build regression;

test: venv												## Локальный запуск тестов
	uv run pytest $(OPTIONS) --alluredir=./allure-results --json-report --json-report-file=logs/results.json --junitxml=test-results.xml

local-test: install                           ## Локальный запуск тестов c поднятием контейнеров
	uv run pytest $(OPTIONS) --alluredir=./allure-results --json-report --json-report-file=logs/results.json --junitxml=test-results.xml

docker-test: .env dirs docker-build up                                                ## Запуск всех тестов с докера
	$(COMPOSE) exec -T tests make test OPTIONS="$(OPTIONS)"

stop_test:
	$(COMPOSE) exec  -T tests killall5 -9 'make test'

report: .env
	allure generate --clean

view:
	allure serve
	#python3 -m http.server -d ./allure-report/ 8080


dirs: ${DIRS_TO_MAKE}

${DIRS_TO_MAKE}:
	mkdir -p ${DIRS_TO_MAKE}

up: .env dirs docker-build
	$(COMPOSE) up -d


down: .env
	cd .
	$(COMPOSE) down

clean: down
	rm -rf ${DIRS_TO_CLEAN}

.env:
	cd .
	printf '\nUID=%s' "`id -u`" >> .env
	printf '\nGID=%s' "`id -g`" >> .env

restart: down up

start: install docker-build up