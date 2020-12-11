from flask import request
from flask_restful import Resource
from .schema import SignUpSchema
from marshmallow import ValidationError


class SignUpView(Resource):
    _schema = SignUpSchema()

    def post(self):
        request_json = request.json
        try:
            user = self._schema.load(data=request_json)
        except ValidationError as e:
            print(e.messages)
            return {}
        else:
            if not user:
                return {}
            else:
                return self._schema.dump(user)


