from flask import request
from flask_restful import Resource

from character.application import List, Create


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
        args = request.get_json()
        character_creation = Create()
        character_creation.values.name = args.get('name')
        character_creation.values.description = args.get('description', None)
        character_creation.values.year_of_birth = args.get('year_of_birth', None)
        character_creation.values.month_of_birth = args.get('month_of_birth', None)
        character_creation.values.day_of_birth = args.get('day_of_birth', None)
        character_creation.values.status = args.get('status')
        character_creation.values.gender = args.get('gender', None)
        character_creation.values.life_status = args.get('life_status')

        result = character_creation.execute()
        if result:
            return '', 201
        else:
            return '', 401

    def put(self):
        pass

    def delete(self):
        pass
