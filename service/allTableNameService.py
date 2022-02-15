from repository.allRepo import allRepo
def allTableNameService(table_name:str)->object:
  if table_name == "data_dict" or table_name == "fdic_fail":
    return allRepo(table_name) 
  else:
    return allRepo("table_"+table_name)

