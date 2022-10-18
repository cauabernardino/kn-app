# Shipments API

CRUD API with Django REST backend and simple Vue.js frontend.

## Requirements

- Docker
- Docker Compose 2+
- Python 3.9+
- npm

## How to run

First, clone the application:
```bash
$ git clone https://github.com/cauabernardino/kn-app.git
$ cd kn-app
```

To start the application in dev mode:
```bash
$ mv .env.sample .env
$ cd client/shipments_client && npm install && cd ../../
$ make build
$ make up
```
- Access `localhost:8080`

To bring down containers:
- `make down`

To run tests:
- `make test`