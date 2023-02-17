import uvicorn
from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from db_utils import *

# init app
app = FastAPI()

# Mount the static files directory at "/static/css"
app.mount("/static", StaticFiles(directory="static"), name="static")


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