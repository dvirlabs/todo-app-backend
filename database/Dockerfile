FROM postgres:latest

WORKDIR /app

COPY init.sql /docker-entrypoint-initdb.d/init.sql

# RUN [[ -e "pg_dump.sql" ]] && cp pg_dump.sql /docker-entrypoint-initdb.d/

EXPOSE 5432

CMD [ "todo_user" ]