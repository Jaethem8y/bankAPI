from repository.singleRepo import singleRepo
# optional start and end ints
# default 0 , 1000
# 
def tableNameService(tableName:str, start:int = 0, end:int = 100000)->object:
  if tableName == "data_dict" or tableName == "fdic_fail":
    return singleRepo(tableName, start, end) # pass start , int, required
  tableNameComplete = "table_"+tableName
  return singleRepo(tableNameComplete, start, end)
