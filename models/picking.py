from blanco.database import Base
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import Enum
import enum


class PickingStatus(enum.Enum):
    INIT = 1
    CONFORM = 2
    FINISH = 3
    CANCEL = 4

class Picking(Base):

    __tablename = "picking"
    id = Column(Integer, primary_key=True, autoincrement=True)
    sn = Column(String(64))
    status = Column(Enum(PickingStatus), default=PickingStatus.INIT)
    user_id = Column(Integer, ForeignKey("user.id"))
    create_at = Column(DateTime)
    update_at = Column(DateTime)