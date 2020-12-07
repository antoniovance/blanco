from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import ForeignKey
from sqlalchemy import Float

from blanco.database import Base


class Sku(Base):
    """sku实际物品"""

    __tablename__ = 'sku'
    id = Column(Integer, primary_key=True)
    name = Column(String(120))
    product_id = Column(Integer, ForeignKey("product.id"))
    color = Column(String(32))
    size = Column(String(32))
    stock = Column(Float)
    unit_id = Column(Integer, ForeignKey("unit.id"))

    def __init__(self, name, product_id, color, size, stock, unit_id):
        self.name = name
        self.product_id = product_id
        self.color = color
        self.size = size
        self.stock = stock
        self.unit_id = unit_id
    

    def __repr__(self):
        return "<sku {}>".format(self.name)
        