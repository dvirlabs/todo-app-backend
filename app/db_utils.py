import psycopg2
import psycopg2.extras
import os

os.chdir('..')

username = os.environ['POSTGRES_USER']
password = os.environ['POSTGRES_PASSWORD']

# Connect to the PostgreSQL database
conn = psycopg2.connect(
    host="localhost",
    port="5432",
    database="TODO-DB",
    user=username,
    password=password
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