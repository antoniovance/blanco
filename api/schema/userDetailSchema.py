from marshmallow import Schema
from marshmallow import fields
from marshmallow import post_load
from marshmallow import pre_dump
from marshmallow import pre_load
from blanco.database import db_session
from models import User


class UserDetailSchema(Schema):
    id = fields.Integer()
    name = fields.String(allow_none=True)
    email = fields.String(allow_none=True)
    birthday = fields.DateTime(format='iso', allow_none=True)
    sex = fields.Integer(allow_none=True)

    def load(self, data, pk):
        data['id'] = pk
        return super(UserDetailSchema, self).load(data)

    @post_load
    def update_user_detail(self, data, **kwargs):
        user = db_session.query(User).filter(User.id == data['id']).first()
        if not user:
            return
        else:
            if getattr(data, 'name', None) is not None:
                user.name = data['name']
            if getattr(data, 'email', None) is not None:
                user.email = data['email']
            db_session.add(user)
            db_session.commit()
            return

    @pre_dump
    def fatch_user(self, pk, **kwargs):
        return db_session.query(User).filter(User.id == pk).first()
