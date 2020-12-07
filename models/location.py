from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey

from blanco.database import Base

class Location(Base):
    """实际摆放位置"""

    __table__ = 'location'
    id = Column(Integer, primary_key=True)
    name = Column(String(120))
    user_id = Column(Integer, ForeignKey('user.id'))
    create_at = Column(DateTime)
    update_at = Column(DateTime)

    def __init__(self, name):
        self.name = name
    
    def __repr__(self):
        return "<Location {}>".format(self.name)