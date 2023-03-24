FROM postgres:latest
ENV POSTGRES_PASSWORD=${POSTGRES_PASSWORD}
ENV POSTGRES_USER=${POSTGRES_USER}
ENV POSTGRES_DB=${POSTGRES_DB}
EXPOSE 5432
COPY create_fixtures.sql /docker-entrypoint-initdb.d/create_fixtures.sql
RUN psql -U $POSTGRES_USER -d $POSTGRES_DB -c "\i create_fixtures.sql"
CMD ["postgres"]