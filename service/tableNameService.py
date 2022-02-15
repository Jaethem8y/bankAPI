from repository.singleRepo import singleRepo

def tableNameService(table_name:str, start:int)->object:
  if table_name == "data_dict" or table_name == "fdic_fail":
    return singleRepo(table_name, start) 
  else:
    tableNameComplete = "table_"+table_name
    return singleRepo(tableNameComplete, start)
