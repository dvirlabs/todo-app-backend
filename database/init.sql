CREATE USER IF NOT EXISTS todo_user WITH PASSWORD '${POSTGRES_PASSWORD}';

CREATE DATABASE todo_db WITH OWNER todo_user;

GRANT ALL PRIVILEGES ON DATABASE todo_db TO todo_user;

\c todo_db todo_user;

CREATE TABLE IF NOT EXISTS tasks(
   id SERIAL PRIMARY KEY,
   task VARCHAR NOT NULL,
   ststus VARCHAR NOT NULL
);