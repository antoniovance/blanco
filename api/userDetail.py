import flask
from flask import request
from flask_restful import Resource
from .schema import UserDetailSchema


class UserDetailView(Resource):
    _schema = UserDetailSchema()

    def get(self, pk):
        return self._schema.dump(pk)

    def post(self, pk):
        request_json = request.json
        self._schema.load(request_json, pk)
        return {}