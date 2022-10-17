SHELL=/bin/bash

up:
	docker compose up -d
down:
	docker compose down -v

.PHONY: up down