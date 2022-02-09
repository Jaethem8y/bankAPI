from fastapi import FastAPI, Request
from service.tableNameService import tableNameService
from postModels.Limit import Limit
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")



@app.get(path="/",response_class=HTMLResponse)
async def getIndex(request:Request):
  return templates.TemplateResponse("index.html",{"request":request})

@app.get(path="/{table_name}")
async def getByTableName(table_name:str):
  return tableNameService(table_name)
  

# @app.post(path="/{table_name}")
# async def postByTableName(table_name:str, body:Limit):
#   return tableNameService(table_name,body.limit1,body.limit2)
  
  
