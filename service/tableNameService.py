from repository.singleRepo import singleRepo

def tableNameService(table_name:str, start:int,end:int,search:str)->object:
  if int(end) - int(start) > 10000 or end == -1 or end <= start:
    end = start + 10000
  print("service:",start,"end:",end)
  if table_name == "data_dict" or table_name == "fdic_fail":
    return singleRepo(table_name, start, end, search) 
  else:
    tableNameComplete = "table_"+table_name
    return singleRepo(tableNameComplete, start, end, search)
