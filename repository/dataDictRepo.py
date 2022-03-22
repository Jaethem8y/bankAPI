from sqlalchemy import MetaData, create_engine, Table, exc
from sqlalchemy.orm import sessionmaker
from key import key

def dataDictRepo(item_code:str,meaning:str)->object:
  engine = create_engine(key)
  metadata = MetaData(engine)
  Session = sessionmaker(bind=engine)
  session = Session()
  try:
    table = Table("data_dict",metadata,autoload=True,autoload_with=engine)
    ret = session.query(table).filter(table.c["item_code"].like("%"+item_code+"%")).filter(table.c["meaning"].like("%"+meaning+"%"))[0:]
    session.close()
    return ret
  except exc.NoSuchTableError:
    session.close()
    return {"invalid query: table does not exist."}



