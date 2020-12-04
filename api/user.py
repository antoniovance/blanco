import flask

from flask import Blueprint
from flask import request
# from flask import current_app

# app = current_app()

user_blueprint = Blueprint('user', __name__, url_prefix='/user')
# app.register_blueprint(user_blueprint)


@user_blueprint.route('/', methods=('GET',))
def info():
    return {'user_id': 1}
