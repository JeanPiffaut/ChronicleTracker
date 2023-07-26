from flask import jsonify
from flask_restful import Resource

from character.application.list import List


class ApiResource(Resource):
    def get(self, character_id):
        character_list = List()
        character_list.fill.id = character_id

        response = character_list.execute()
        if response is not False:
            return response, 200
        else:
            errors = character_list.get_errors()
            return str(errors), 400

    def post(self):
        pass

    def put(self):
        pass

    def delete(self):
        pass
