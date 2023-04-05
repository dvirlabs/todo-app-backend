FROM todo-db:v1.0

WORKDIR /app

COPY init.sql /docker-entrypoint-initdb.d/init.sql

EXPOSE 5432

CMD [ "postgres" ]