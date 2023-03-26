FROM postgres:latest

WORKDIR /app

COPY create_fixtures.sql /docker-entrypoint-initdb.d/create_fixtures.sql

EXPOSE 5432

CMD [ "postgres" ]