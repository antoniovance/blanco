from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import Text
from sqlalchemy import Boolean
from sqlalchemy import ForeignKey

from blanco.database import Base


class Location(Base):
    """实际摆放位置"""

    __tablename__ = 'location'
    id = Column(Integer, primary_key=True)
    name = Column(String(120))
    description = Column(Text)
    user_id = Column(Integer, ForeignKey('user.id'))
    avatar = Column(String(120), doc="位置图片")
    is_delete = Column(Boolean, default=False)
    create_at = Column(DateTime)
    update_at = Column(DateTime)

    def __init__(self, name, user_id, create_at, update_at):
        self.name = name
        self.user_id = user_id
        self.create_at = create_at
        self.update_at = update_at
    
    def __repr__(self):
        return "<Location {}>".format(self.name)