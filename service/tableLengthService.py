from repository.tableLengthRepo import tableLengthRepo
def tableLengthService(table_name:str)->object:
  if table_name == "data_dict" or table_name == "fdic_fail":
    return tableLengthRepo(table_name) 
  else:
    table_name_complete = "table_"+table_name
    return tableLengthRepo(table_name_complete)
