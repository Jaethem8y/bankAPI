from repository.singleRepo import singleRepo

def tableNameService(table_name:str,start:int,end:int,bank_id:str,year:str,quarter:str,score:str)->object:
  if int(end) - int(start) > 10000 or end == -1 or end <= start:
    end = start + 10000
  print("service:",start,"end:",end)
  table = table_name
  table_name = "table_"+table_name
  return singleRepo(table_name,start,end,bank_id,year,quarter,score,table) 



