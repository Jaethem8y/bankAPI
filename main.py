from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse
from fastapi.middleware import Middleware
from fastapi.middleware.cors import CORSMiddleware

import uvicorn
from service.dataDictService import dataDictService

from service.tableNameService import tableNameService
from service.showTableService import showTableService
from service.allTableNameService import allTableNameService
from service.descriptionTableService import descriptionTableService
from service.tableLengthService import tableLengthService



# from postModels.Limit import Limit
description = """
## If the text contains typo or ambiguous, please contact Jaehyeok Choi at jaehyeok.choi@drake.edu for change or explanation.
## What is this
Bank API developed for Drake University Economics Data Science Team Led by Dr. Eric Manley,
 \nCreators: Jaehyeok Choi, Jacob Danner

## Why this API was made
This api serves as bridge for Bank Fail Database built by Dr. Eric Manley and the web client

## Recommentation
Try to get request to "/data_dict" for the "metadata" or the description for what each table name means to query. \n
Every table name should be able to query by "/{table_name}" for example "/CALL8786" or "/data_dict" \n
**IMPORTANT** \n
It is critical for user to first get the length of the table, the number of the rows, and get a loop to request the complete table using appropriate query-string. \n
Some of the tables have over million rows. In order to keep server from dying, the request without query string will in default return first 10,000 rows from table. \n
if table has less than 10,000 rows, then the regular query without query-string would work as it would return entire rows for the tables. 

## What can you do with this API

* **get request to "/"** - will direct you to this doc
* **get request to "/tables"** - will list you all the tables in this database
* **get request to "/{table_names}" - such as "/CALL8786"** - will give you the first 10000 data from the specified table
* **get request to "/{table_names}?start=x" - such as "/CALL8786/start=10000"** will query data starting from row 10000 to row 20000
* **get request to "/describe/{table_name}" - such as "/describe/table_name"** will return a result equivalen of describe table_name in mysql
* **get request to "/length/{table_name}" - "such as /length/CALL8786"** will return the length of the table (number of rows in table)

## Advanced Search for /data_dict
* when searching for /data_dict, the item_code and meaning can be specified for the search purpose
* **/data_dict?item_code=RCFA ** will return all the data_dict content which item_code column contains "RCFA"
* **/data_dict?meaning=total ** will return all the data_dict content which meaning column contains "total"
* **/data_dict?item_code=RCFA&meaing=total ** will return all data_dict content which column item_code contains "RCFA" and column meaning contains "total"

## Advanced Search for /{table_name}
* when searching for table_name, there are start, end, bank_id, year, quarter, and score that user can specify
* start and end is just a numeric values for which index user wants to search
* for example, **/CALL8786?start=100&end=800** will return 30th to 800th rows from CALL8786 table.
* the range of start and end cannot exceed 10000. For example, if start = 10 and end = 10000000, then automatically, it will return rows 10 to 10010 instead of 10 to 100000000
* when bank_id, year, quarter, and score is specified, it will return result that contains such value
* for example, **/CALL8786?bank_id=28&year=1988&quarter=3&score=2** will return all the result that bank_id contains 1988, quarter contains 3, and CALL8786 score contains 2.

"""

tags_metadata = [
  {
    "name": "tables",
    "description":"Returns the lists of tables that are in bankDB",
  },
  {
    "name":"data_dict",
    "description":"returns all content from data_dict table",
  },
  {
    "name":"table_name",
    "description":"When the table_name is replaced by table name form data_dict query, it returns the content of that table",
  },
  {
    "name":"describe",
    "description":"This request will return the description of the table that one put after such as /description/CALL8786 will display the description of table CALL8786",
  },
  {
    "name":"length",
    "description":"This request will return the number of the rows in table, length, of desired table", 
  }
]


middleware = [
    Middleware(
        CORSMiddleware,
        allow_origins=['*'],
        allow_credentials=True,
        allow_methods=['*'],
        allow_headers=['*']
    )
]
app = FastAPI(
  title="Bank API",
  description=description,
  version="1.0.0",
  openapi_tags=tags_metadata,
  middleware=middleware
)

@app.get(path="/")
async def getIndex(request:Request):
  return RedirectResponse("/docs")

@app.get(path="/tables",tags=["tables"])
async def getTableColName():
  return showTableService()

@app.get(path="/data_dict",tags=["data_dict"])
async def getDataDictTable(item_code:str="", meaning:str=""):
  return  dataDictService(item_code,meaning)
  

@app.get(path="/{table_name}",tags=["table_name"])
async def getRowsByTableName(table_name:str,start:int=0,end:int=-1,bank_id:str="",year:str="",quarter="",score=""):
  return tableNameService(table_name,start,end,bank_id,year,quarter,score)

@app.get(path="/describe/{table_name}",tags=["describe"])
async def getTableDescribtion(table_name:str):
  return descriptionTableService(table_name)

@app.get(path="/length/{table_name}",tags=["length"])
async def getTableLength(table_name:str):
  return tableLengthService(table_name)
# @app.get(path="/all/{table_name}")
# async def getAllRowsByTableName(table_name):
#   return allTableNameService(table_name)




# @app.post(path="/{table_name}")
# async def postByTableName(table_name:str, body:Limit):
#   return tableNameService(table_name,body.limit1,body.limit2)
  
  
