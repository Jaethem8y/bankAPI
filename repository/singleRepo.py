import os 
from sqlalchemy import MetaData, create_engine,Table
from sqlalchemy.orm import sessionmaker
from key import key

# start and end
def singleRepo(tableName:str, start:int, end:int)->object:
  engine = create_engine(key)
  metadata = MetaData(engine)
  Session = sessionmaker(bind=engine)
  session = Session()
  table = Table(tableName,metadata,autoload=True,autoload_with=engine)
  return session.query(table)[start:end] # [start:end], error handle, internal server error. try except 



