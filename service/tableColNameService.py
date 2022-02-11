from repository.singleRepo import singleRepo

def tableNameService(tableName:str, start:int = 0, end:int = 100000)->object:
  if tableName == "data_dict" or tableName == "fdic_fail":
    return singleRepo(tableName, start, end) 
  else:
    tableNameComplete = "table_"+tableName
    return singleRepo(tableNameComplete, start, end)
