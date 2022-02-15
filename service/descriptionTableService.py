from repository.describtionRepo import descriptionRepo

def descriptionTableService(table_name:str)->object:
  if table_name == "data_dict" or table_name == "fdic_fail":
    return descriptionRepo(table_name) 
  else:
    tableNameComplete = "table_"+table_name
    return descriptionRepo(tableNameComplete)