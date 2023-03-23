FROM postgres:latest
ENV POSTGRES_PASSWORD=${POSTGRES_PASSWORD}
ENV POSTGRES_USER=${POSTGRES_USER}
ENV POSTGRES_DB=${DATABASE_NAME}
COPY create_fixtures.sql /docker-entrypoint-initdb.d/create_fixtures.sql