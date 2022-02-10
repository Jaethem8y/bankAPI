from sqlalchemy import MetaData, create_engine, Table, exc
from sqlalchemy.orm import sessionmaker
from key import key

def singleRepo(tableName:str, start:int, end:int)->object:
  engine = create_engine(key)
  metadata = MetaData(engine)
  Session = sessionmaker(bind=engine)
  session = Session()
  try:
    table = Table(tableName,metadata,autoload=True,autoload_with=engine)
    return session.query(table)[start:end]
  except exc.NoSuchTableError:
    return {"invalid query: table does not exist."}



