from ensurepip import version
from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse
from fastapi.openapi.utils import get_openapi

from service.tableNameService import tableNameService
from service.showTableService import showTableService
from service.allTableNameService import allTableNameService
from service.descriptionTableService import descriptionTableService
from service.tableLengthService import tableLengthService
# from postModels.Limit import Limit
description = """
## What is this
Bank API developed for Drake University Economics Data Science Team Led by Dr. Eric Manley,
 \nContributers: Jaehyeok Choi, Jacob Danner

## Why this API was made
This api serves as bridge for Bank Fail Database built by Dr. Eric Manley and the web client


## What can you do with this API

* **get request to "/"** - will direct you to this doc
* **get request to "/tables"** - will list you all the tables in this database
* **get request to "/{table_names}" - such as "/CALL8786"** - will give you the first 10000 data from the specified table
* **get request to "/{table_names}?start=x" - such as "/CALL8786/start=10000"** will query data starting from row 10000 to row 20000
* **get request to "/describe/{table_name}" - such as "/describe/table_name"** will return a result equivalen of describe table_name in mysql
* **get request to "/length/{table_name}" - "such as /length/CALL8786"** will return the length of the table (number of rows in table)
"""


app = FastAPI(
  title="Bank API",
  description=description,
  version="1.0.0"
)


@app.get(path="/")
async def getIndex(request:Request):
  return RedirectResponse("/docs")

@app.get(path="/tables")
async def getTableColName():
  return showTableService()

@app.get(path="/{table_name}")
async def getRowsByTableName(table_name:str,start:int=0):
  return tableNameService(table_name,start)

@app.get(path="/describe/{table_name}")
async def getTableDescribtion(table_name:str):
  return descriptionTableService(table_name)

@app.get(path="/length/{table_name}")
async def getTableLength(table_name:str):
  return tableLengthService(table_name)
# @app.get(path="/all/{table_name}")
# async def getAllRowsByTableName(table_name):
#   return allTableNameService(table_name)




# @app.post(path="/{table_name}")
# async def postByTableName(table_name:str, body:Limit):
#   return tableNameService(table_name,body.limit1,body.limit2)
  
  
