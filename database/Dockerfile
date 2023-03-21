FROM postgres:latest
ENV POSTGRES_PASSWORD=changeme
ENV POSTGRES_USER=changeuser
ENV POSTGRES_DB=database
COPY create_fixtures.sql /docker-entrypoint-initdb.d/create_fixtures.sql