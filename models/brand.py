from blanco.database import Base
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import DateTime
from sqlalchemy import Enum

import enum


class BrandType(enum.Enum):
    private = 1
    public = 2


class Brand(Base):
    __tablename__ = "brand"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(64))
    type = Column(Enum(BrandType), default=BrandType.private, doc="品牌类型")
    official_link = Column(String(120), nullable=True, doc="官网的链接")
    user_id = Column(Integer, ForeignKey("user.id"))
    create_at = Column(DateTime)
    update_at = Column(DateTime)
