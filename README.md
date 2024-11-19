# Philly Bike Action Administration, Bridges, and Planning

## Running Locally
1. Install Docker engine and docker compose
   1. [Docker Engine](https://docs.docker.com/engine/install/)
   2. [Docker Compose](https://docs.docker.com/compose/install/)
2. Run `make serve` this will launch all necessary containers including Redis, Postgres, Celery workers, web server, etc.
3. Access:
   1. the website at `localhost:8000`
   2. Django admin at `localhost:8000/admin`.
   3. Mail Server at `localhost:1080/#/`
