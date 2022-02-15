from sqlalchemy import MetaData, create_engine, Table, exc
from sqlalchemy.orm import sessionmaker
from key import key

def descriptionRepo(table_name:str)->object:
  engine = create_engine(key)
  Session = sessionmaker(bind=engine)
  session = Session()
 
  return session.execute("describe "+table_name).all()



