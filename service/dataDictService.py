from repository.dataDictRepo import dataDictRepo

def dataDictService(item_code:str="",meaning:str="")->object:
  return dataDictRepo(item_code,meaning)



