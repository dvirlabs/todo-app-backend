FROM postgres:latest

WORKDIR /app

ARG POSTGRES_PASSWORD

ENV POSTGRES_PASSWORD=${POSTGRES_PASSWORD}

COPY create_fixtures.sql /docker-entrypoint-initdb.d/create_fixtures.sql
COPY .env .

EXPOSE 5432

CMD [ "postgres" ]