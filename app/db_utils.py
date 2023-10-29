import psycopg2
import psycopg2.extras
import os
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '..', '.env')
load_dotenv(dotenv_path)

db_username = os.environ.get('POSTGRES_USER')
db_password = os.environ.get('POSTGRES_PASSWORD')
db_host = os.environ.get('POSTGRES_HOST')
postgres_port = os.environ.get('POSTGRES_PORT')
database_name = os.environ.get('POSTGRES_DB')


print (database_name)

# Connect to the PostgreSQL database
conn = psycopg2.connect(
    host=db_host,
    port=postgres_port,
    database=database_name,
    user=db_username,
    password=db_password
)

# get the data from the DB in json format
cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

# select data from DB
def get_data(query):
    try:

        # Run the query and fetch the results
        cur.execute(query)
        data = cur.fetchall()
        return data
    except Exception as error:
        print(error)
        
# update the DB        
def set_data(query):
    try:
        # Run the query and fetch the results
        cur.execute(query)
        conn.commit()
        return "Database was updated"
    except Exception as error:
        print(error)
