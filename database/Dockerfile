FROM postgres:latest

WORKDIR /app

COPY init_db.sh /docker-entrypoint-initdb.d/

RUN chmod +x /docker-entrypoint-initdb.d/init_db.sh

# RUN /docker-entrypoint-initdb/init_db.sh

# RUN chmod 777 /usr/local/bin/docker-entrypoint.sh \
#     && ln -s /usr/local/bin/docker-entrypoint.sh /

# RUN [[ -e "pg_dump.sql" ]] && cp pg_dump.sql /docker-entrypoint-initdb.d/

EXPOSE 5432

CMD [ "postgres" ]