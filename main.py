from fastapi import FastAPI, Request
from service.tableNameService import tableNameService
from service.showTableService import showTableService
from service.allTableNameService import allTableNameService
from service.descriptionTableService import descriptionTableService
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

@app.get(path="/tables")
async def getTableColName():
  return showTableService()

@app.get(path="/{table_name}")
async def getRowByTableName(table_name):
  return tableNameService(table_name)

@app.get(path="/all/{table_name}")
async def getAllRowsByTableName(table_name):
  return allTableNameService(table_name)

@app.get(path="/describe/{table_name}")
async def getTableDescribtion(table_name):
  return descriptionTableService(table_name)


# @app.post(path="/{table_name}")
# async def postByTableName(table_name:str, body:Limit):
#   return tableNameService(table_name,body.limit1,body.limit2)
  
  
