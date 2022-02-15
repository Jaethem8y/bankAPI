from sqlalchemy import MetaData, create_engine, Table, exc
from sqlalchemy.orm import sessionmaker
from key import key

def singleRepo(table_name:str, start:int=0)->object:
  engine = create_engine(key)
  metadata = MetaData(engine)
  Session = sessionmaker(bind=engine)
  session = Session()
  end = start + 10000
  print("start:",start,"end:",end)
  try:
    table = Table(table_name,metadata,autoload=True,autoload_with=engine)
    return session.query(table)[start:end]
  except exc.NoSuchTableError:
    return {"invalid query: table does not exist."}



