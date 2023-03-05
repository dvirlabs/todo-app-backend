import uvicorn
from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
# from fastapi.templating import Jinja2Templates
from db_utils import *
import os

# init app
app = FastAPI()

# Mount the static files directory at "/static"
script_dir = os.path.dirname(__file__)
st_abs_file_path = os.path.join(script_dir, "static/")
app.mount("/static", StaticFiles(directory=st_abs_file_path), name="static")

# templates = Jinja2Templates(directory="templates")


# ================ Main ================

@app.get("/")
async def index():
    return FileResponse("index.html")

# ======================================

# ================ Get the data of the table ================
  
@app.get("/table")
async def get_result():

  # Run a query and fetch the results using the `get_data` function
  query = "SELECT * FROM tasks"
  
  results = get_data(query)
   
  # Return the results as a JSON response
  return {"results": results}
# ======================================

# ================ Add new row to table ================

@app.post("/add_row")
async def insert_row_to_table(row : dict):
  
  # Run a query and fetch the results using the `get_data` function
  query = "INSERT INTO tasks (task , status) VALUES ('"+ row['task'] +"','"+ row['status']+"')"
  
  results = set_data(query)
   
  # Return the results as a JSON response 
  return {"results": results}
# ======================================

# ================ Delete row from the table ================

@app.delete("/delete_row")
async def delete_row_from_table(row : int):
  query = "DELETE FROM tasks WHERE id =  ('"+ str(row)+"')"
  
  results = set_data(query)
  return {"results": results}
# ======================================

# ================ Clear the data of the table ================

@app.delete("/clear_table")
async def truncate_table():
  
  # This action will clear all the data from the table
  query = "TRUNCATE tasks RESTART IDENTITY"
  # query = "ALTER SEQUENCE tasks_id_seq RESTART WITH 1"
  results = set_data(query)
  
  # Return the results as a JSON response
  return {"results": results}
# ======================================

# ================ Create new table ================

@app.post("/add_table{table_name}")
async def createNewTable(table_name: str):
  
  query = "CREATE TABLE "+ (table_name) + "( id SERIAL PRIMARY KEY, task VARCHAR NOT NULL , status VARCHAR NOT NULL );"
  
  results = set_data(query)
  
  return {"results": results}

# ======================================











if __name__ == '__main__':
  uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True, access_log=False)