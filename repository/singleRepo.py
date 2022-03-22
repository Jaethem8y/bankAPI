from sqlalchemy import MetaData, create_engine, Table, exc
from sqlalchemy.orm import sessionmaker
from key import key

def singleRepo(table_name:str,start:int,end:int,bank_id:str,year:str,quarter:str,score:str,table_n)->object:
  engine = create_engine(key)
  metadata = MetaData(engine)
  Session = sessionmaker(bind=engine)
  session = Session()
  try:
    table = Table(table_name,metadata,autoload=True,autoload_with=engine)
    ret = session.query(table).filter(table.c["bank_id"].like("%"+bank_id+"%")).filter(table.c["year"].like("%"+year+"%")).filter(table.c["quarter"].like("%"+quarter+"%")).filter(table.c[table_n].like("%"+score+"%"))[start:end]
    session.close()
    return ret
  except exc.NoSuchTableError:
    session.close()
    return {"invalid query: table does not exist."}



