from sqlalchemy import MetaData, create_engine, Table, exc
from sqlalchemy.orm import sessionmaker
from key import key

def allRepo(table_name:str)->object:
  engine = create_engine(key)
  metadata = MetaData(engine)
  Session = sessionmaker(bind=engine)
  session = Session()
  try:
    start = 0
    end = 10000
    ret = []
    table = Table(table_name,metadata,autoload=True,autoload_with=engine)
    while True:
      temp = session.query(table)[start:end]
      if temp == []:
        return ret
      print(start)
      ret.extend(temp)
      start = end
      end += 10000
  except exc.NoSuchTableError:
    return {"invalid query: table does not exist."}



