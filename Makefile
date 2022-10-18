SHELL=/bin/bash

up:
	docker compose up -d
down:
	docker compose down -v
rs:
	docker compose restart
build:
	docker compose build
test:
	docker compose run --rm api \
		sh -c "python manage.py wait_for_db && python manage.py test -v 2"

.PHONY: up down rs build test