from repository.describtionRepo import descriptionRepo

def descriptionTableService(tableName:str)->object:
  if tableName == "data_dict" or tableName == "fdic_fail":
    return descriptionRepo(tableName) 
  else:
    tableNameComplete = "table_"+tableName
    return descriptionRepo(tableNameComplete)