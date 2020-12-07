import os

from flask import Flask
from flask_restful import Api
from api import UserInfo

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'blanco.sqlite'),
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)
    

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # register app
    # from api.user import user_blueprint
    # app.register_blueprint(user_blueprint)

    api = Api(app=app)
    api.add_resource(UserInfo, "/user/<int:pk>")

    @app.route("/")
    def hi():
        return "hi"

    return app

