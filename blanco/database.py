from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("sqlite:///test.sqlite3", convert_unicode=True)
metadata = MetaData()
db_session = scoped_session(
    sessionmaker(
        autocommit=False, autoflush=False, bind=engine
        )
    )

Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
    # metadata.create_all(bind=engine)
    Base.metadata.create_all(engine)
    # Base.metadata.drop_all(engine)