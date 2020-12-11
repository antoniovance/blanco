from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import ForeignKey
from sqlalchemy import Float
from sqlalchemy import DateTime
from sqlalchemy import Enum
from blanco.database import Base

import enum


class SkuGainType(enum.Enum):
    PERCHASE = 1
    GIFT = 2
    EXCHANEG = 3


class Sku(Base):
    """sku实际物品"""
    __tablename__ = 'sku'

    id = Column(Integer, primary_key=True)
    name = Column(String(120))
    product_id = Column(Integer, ForeignKey("product.id"))
    color = Column(String(32))
    size = Column(String(32))
    stock = Column(Float, doc="库存数值")
    unit_id = Column(Integer, ForeignKey("unit.id"), doc='单位')
    cost_price = Column(Float, default=0, doc='累计采购价格')
    gain_type = Column(Enum(SkuGainType), nullable=True, doc="获得的方式")
    expire_at = Column(DateTime, nullable=True, doc="过期时间")
    create_at = Column(DateTime, doc="创建时间")
    update_at = Column(DateTime, doc="更新时间")

    def __init__(self, name, product_id, color, size, stock, unit_id):
        self.name = name
        self.product_id = product_id
        self.color = color
        self.size = size
        self.stock = stock
        self.unit_id = unit_id

    def __repr__(self):
        return "<sku {}>".format(self.name)
        