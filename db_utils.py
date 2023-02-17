import psycopg2
import psycopg2.extras


# Connect to the PostgreSQL database
conn = psycopg2.connect(
    host="192.168.1.207",
    database="TODO-DB",
    user="python",
    password="lab1234"
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
    except Exception as error:
        print(error)
