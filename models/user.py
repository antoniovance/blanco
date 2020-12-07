from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from blanco.database import Base

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer,primary_key=True)
    name = Column(String(120), unique=True)
    password = Column(String(64))
    email = Column(String(60), unique=True)
    
    def __repr__(self):
        return "<User {}>".format

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password


        
