from repository.allRepo import allRepo
def allTableNameService(tableName:str)->object:
  if tableName == "data_dict" or tableName == "fdic_fail":
    return allRepo(tableName) 
  else:
    return allRepo("table_"+tableName)

