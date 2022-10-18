SHELL=/bin/bash

up:
	docker compose up -d
down:
	docker compose down -v
rs:
	docker compose restart
build:
	docker compose build

.PHONY: up down rs build