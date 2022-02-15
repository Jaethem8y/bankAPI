from sqlalchemy import MetaData, create_engine, Table, exc
from sqlalchemy.orm import sessionmaker
from key import key

def allRepo()->object:
  engine = create_engine(key)
  metadata = MetaData(engine)
  Session = sessionmaker(bind=engine)
  session = Session()
  try:
    return len(session.execute("show tables").all())
  except exc.NoSuchTableError:
    return {"invalid query: table does not exist."}

print(allRepo())