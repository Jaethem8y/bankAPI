import os 
from sqlalchemy import MetaData, create_engine,Table
from sqlalchemy.orm import sessionmaker
from key import key


def singleRepo(tableName:str)->object:
  engine = create_engine(key)
  metadata = MetaData(engine)
  Session = sessionmaker(bind=engine)
  session = Session()
  table = Table(tableName,metadata,autoload=True,autoload_with=engine)
  return session.query(table).all()



