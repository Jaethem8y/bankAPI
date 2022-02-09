from repository.singleRepo import singleRepo
# optional start and end ints
# default 0 , 1000
# 
def tableNameService(tableName:str)->object:
  if tableName == "data_dict" or tableName == "fdic_fail":
    return singleRepo(tableName) # pass start , int, required
  tableNameComplete = "table_"+tableName
  return singleRepo(tableNameComplete)
