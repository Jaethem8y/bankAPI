from repository.singleRepo import singleRepo

def tableNameService(tableName:str)->object:
  if tableName == "data_dict" or tableName == "fdic_fail":
    return singleRepo(tableName)
  tableNameComplete = "table_"+tableName
  return singleRepo(tableNameComplete)
