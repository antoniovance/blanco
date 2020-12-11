from marshmallow import Schema
from marshmallow import fields
from marshmallow import post_load
from models.user import User
from blanco.database import db_session


class SignInSchema(Schema):
    name = fields.String()
    password = fields.String()

    @post_load
    def sign_in_user(self, data, **kwargs):
        if db_session.query(User).filter(User.name==data['name'], User.password==data['password']):
            return True
        else:
            return False

