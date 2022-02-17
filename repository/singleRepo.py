from sqlalchemy import MetaData, create_engine, Table, exc
from sqlalchemy.orm import sessionmaker
from key import key

def singleRepo(table_name:str, start:int,end:int,search_col:str,search:str)->object:
  engine = create_engine(key)
  metadata = MetaData(engine)
  Session = sessionmaker(bind=engine)
  session = Session()
  print("repo:",start,"end:",end, "search", search)
  try:
    table = Table(table_name,metadata,autoload=True,autoload_with=engine)
    print("search_col",search_col)
    if search_col == "":
      return session.query(table)[start:end]
    return session.query(table).filter(table.c[search_col].like("%"+search+"%"))[start:end]
  except exc.NoSuchTableError:
    return {"invalid query: table does not exist."}



