from sqlalchemy import MetaData, create_engine, Table, exc
from sqlalchemy.orm import sessionmaker
from key import key

def tableLengthRepo(table_name:str)->object:
  engine = create_engine(key)
  Session = sessionmaker(bind=engine)
  metadata = MetaData(engine)
  session = Session()
  table = Table(table_name,metadata,autoload=True,autoload_with=engine)
  try:
    ret = session.query(table).count()
    session.close()
    return ret
  except exc.NoSuchTableError:
    session.close()
    return {"invalid query: table does not exist."}



