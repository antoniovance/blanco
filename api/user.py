import flask

from flask import Blueprint
from flask import request
from flask import g
from models.user import User
from flask_restful import Resource

user_blueprint = Blueprint('user', __name__, url_prefix='/user')
# app.register_blueprint(user_blueprint)


# @user_blueprint.route('/', methods=('GET',))
# def info():
#     user = User
#     return {'user_id': 1}

class UserInfo(Resource):
    def get(self, pk):
        return {'user_id': pk}