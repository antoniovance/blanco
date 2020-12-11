from flask_restful import Resource
from flask_restful import reqparse
from flask import request
from .schema import SignInSchema

parser = reqparse.RequestParser()


class SignInView(Resource):
    """
    登录接口
    """
    _schema = SignInSchema()

    def post(self):
        json = request.json
        result = self._schema.load(json)
        return {"success": result}
