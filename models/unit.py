from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Column

from blanco.database import Base


class Unit(Base):
    """单位"""

    __tablename__ = 'unit'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<unit {}>'.format(self.name)
    