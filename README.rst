poetry run cli webapi alembic initrevision --message "Init candidate base" --branch-label=candidate --version-path=dhuni_tech/candidate


poetry run cli webapi alembic makemigrations --branch-label=candidate  --message "create migrations"

poetry run cli webapi alembic migrate heads

docker exec -it dhuni_tech psql -U postgres

