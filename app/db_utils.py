import psycopg2
import psycopg2.extras
import os
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '..', '.env')
load_dotenv(dotenv_path)

username = os.environ.get('POSTGRES_USER')
password = os.environ.get('POSTGRES_PASSWORD')
postgres_host = os.environ.get('POSTGRES_HOST')
postgres_port = os.environ.get('POSTGRES_PORT')
database_name = os.environ.get('POSTGRES_DB')

print (postgres_host)

# Connect to the PostgreSQL database
conn = psycopg2.connect(
    host="192.168.1.16",
    port="5432",
    database="todo_db",
    user="todo_user",
    password="Aa123456"    
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
