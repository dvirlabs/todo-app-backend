FROM postgres:latest

WORKDIR /app

COPY init.sql /docker-entrypoint-initdb.d/init.sql

EXPOSE 5432

CMD [ "postgres" ]