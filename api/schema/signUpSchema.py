from marshmallow import Schema
from marshmallow import fields
from marshmallow import post_load
from models.user import User
from blanco.database import db_session


class SignUpSchema(Schema):
    name = fields.String()
    password = fields.String()
    email = fields.String(allow_none=True)
    avatar = fields.String(allow_none=True)
    birthday = fields.Date(allow_none=True)
    sex = fields.Integer(allow_none=True)

    @post_load
    def sign_up_user(self, data, **kwargs):
        print(db_session.query(User).filter(
                User.name == data['name']).count())
        if db_session.query(User).filter(
                User.name == data['name']).count():
            return {}
        else:
            user = User(**data)
            db_session.add(user)
            db_session.commit()
            return user