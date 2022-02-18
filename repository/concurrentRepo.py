from sqlalchemy import MetaData, create_engine, Table, exc
from sqlalchemy.orm import sessionmaker
from key import key

def concurrentRepo(table_name):
  engine = create_engine(key)
  metadata = MetaData(engine)
  Session = sessionmaker(bind=engine)
  session = Session()
  try:
    table = Table(table_name,metadata,autoload=True,autoload_with=engine)
    return session.query(table).all()
  except exc.NoSuchTableError:
    return {"invalid query: table does not exist."}

