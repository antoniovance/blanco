from flask_restful import Resource
from flask import request
from .schema import LocationEditSchema


class LocationEditView(Resource):

    def get(self):
        request_json = request.json()
        _schema = LocationEditSchema()
        data = _schema.dump(request_json)
        return data

    def post(self):
        request_json = request.json
        _schema = LocationEditSchema()
        data = _schema.load(request_json)
        return data

    def put(self):
        request_json = request.json
        _schema = LocationEditSchema()
        data = _schema.load(request_json)
        return data

    def delete(self):
        request_json = request.json
        _schema = LocationEditSchema()
        data = _schema.load(request_json)
        return data
