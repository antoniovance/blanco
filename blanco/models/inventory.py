from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Float
from sqlalchemy import ForeignKey

from blanco.database import Base


class Inventory(Base):
    id = Column(Integer, primary_key=True)
    location_id = Column(Integer, ForeignKey('location.id'))
    product_id = Column(Integer, ForeignKey('product_id'))
    stock = Column(Float)
    unit_id = Column(Integer, ForeignKey('unit.id'))

    def __init__(self, location_id, product_id, stock, unit_id):
        self.location_id = location_id
        self.product_id = product_id
        self.stock = stock
        self.unit_id = unit_id
    
    def __repr__(self):
        return "<inventory {}>".format(self.id)