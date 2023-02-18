import uvicorn
from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from db_utils import *
import os

# init app
app = FastAPI()

# Mount the static files directory at "/static"
script_dir = os.path.dirname(__file__)
st_abs_file_path = os.path.join(script_dir, "static/")
app.mount("/static", StaticFiles(directory=st_abs_file_path), name="static")


@app.get("/")
async def index():
    return FileResponse("index.html")
  
  
@app.get("/table")
async def get_result():
  
  # Run a query and fetch the results using the `get_data` function
  query = "SELECT * FROM tasks"
  results = get_data(query)
   
  # Return the results as a JSON response
  return {"results": results}




if __name__ == '__main__':
  uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True, access_log=False)