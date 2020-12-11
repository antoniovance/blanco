from blanco.database import Base
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import Enum
from sqlalchemy import Text
from sqlalchemy import Boolean
import enum


class PickingStatus(enum.Enum):
    INIT = 1
    CONFORM = 2
    FINISH = 3
    CANCEL = 4


class PickingDirectionType(enum.Enum):
    IN = 1
    OUT = 2


class Picking(Base):

    __tablename = "picking"
    id = Column(Integer, primary_key=True, autoincrement=True)
    sn = Column(String(64))
    status = Column(Enum(PickingStatus), default=PickingStatus.INIT)
    user_id = Column(Integer, ForeignKey("user.id"))
    direction_type = Column(Enum(PickingDirectionType))
    create_at = Column(DateTime)
    update_at = Column(DateTime)
    remark = Column(Text, doc="备注")

    def __init__(self, sn, status, user_id, direction_type, create_at, update_at, remark):
        self.sn = sn
        self.status = status
        self.user_id = user_id
        self.direction_type = direction_type
        self.create_at = create_at
        self.update_at = update_at
        self.remark = remark

    def __repr__(self):
        return "<picking {}>".format(self.id)
