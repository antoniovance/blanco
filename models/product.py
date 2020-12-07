from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import DateTime
from sqlalchemy import Column
from sqlalchemy import Text
from sqlalchemy import Enum
from sqlalchemy import Float
from sqlalchemy import ForeignKey

from blanco.database import Base

import enum

class ProductStatusEnum(enum.Enum):
    offline = 1
    online = 2

class Product(Base):
    """抽象出来的物品"""

    __tablename__ = 'product'
    id = Column(Integer, primary_key=True)
    name = Column(String(120))
    intro = Column(Text)
    status = Column(Enum(ProductStatusEnum))
    stock = Column(Float, doc="数量的总量")
    unit_id = Column(Integer, ForeignKey('unit.id'))
    
    def __init__(self, name, intro, status, stock, unit_id):
        self.name = name
        self.intro = intro
        self.status = status
        self.stock = stock
        self.unit_id = unit_id
    
    def __repr__(self):
        return "<product {}>".format(self.name)


    


    
    

