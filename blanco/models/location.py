from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Column

from blanco.database import Base

class Location(Base):
    id = Column(Integer, primary_key=True)
    name = Column(String(120))

    def __init__(self, name):
        self.name = name
    
    def __repr__(self):
        return "<Location {}>".format(self.name)