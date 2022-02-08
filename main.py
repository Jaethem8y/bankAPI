from fastapi import FastAPI, Request
from service.tableNameService import tableNameService
from postModels.Limit import Limit

app = FastAPI()

@app.get(path="/")
async def getIndex():
  return "Hello"

@app.get(path="/{table_name}")
async def getByTableName(table_name:str):
  return tableNameService(table_name)
  

# @app.post(path="/{table_name}")
# async def postByTableName(table_name:str, body:Limit):
#   return tableNameService(table_name,body.limit1,body.limit2)
  
  
