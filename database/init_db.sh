#!/bin/bash

set -e

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
    CREATE TABLE tasks(
      id SERIAL PRIMARY KEY,
      task VARCHAR NOT NULL,
      status VARCHAR NOT NULL
    );
EOSQL