from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse
from service.tableNameService import tableNameService
from service.showTableService import showTableService
from service.allTableNameService import allTableNameService
from service.descriptionTableService import descriptionTableService
from service.tableLengthService import tableLengthService
# from postModels.Limit import Limit


app = FastAPI()

@app.get(path="/")
async def getIndex(request:Request):
  return RedirectResponse("/docs")

@app.get(path="/tables")
async def getTableColName():
  return showTableService()
@app.get(path="/length/{table_name}")
async def getTableLength(table_name:str):
  return tableLengthService(table_name)
@app.get(path="/{table_name}")
async def getRowsByTableName(table_name:str,start:int=0,end:int=10000):
  return tableNameService(table_name,start,end)

# @app.get(path="/all/{table_name}")
# async def getAllRowsByTableName(table_name):
#   return allTableNameService(table_name)

@app.get(path="/describe/{table_name}")
async def getTableDescribtion(table_name:str):
  return descriptionTableService(table_name)


# @app.post(path="/{table_name}")
# async def postByTableName(table_name:str, body:Limit):
#   return tableNameService(table_name,body.limit1,body.limit2)
  
  
