from flask import request, jsonify
from flask_restful import Resource

from character.application import List, Create
from common.misc import response_structure


class ApiResource(Resource):
    def get(self, character_id):
        character_list = List()
        character_list.fill.id = character_id

        response = character_list.execute()
        if response is not False:
            return response_structure(200, response)
        else:
            errors = character_list.get_errors()
            return response_structure(400, errors)

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
            return response_structure(201)
        else:
            return response_structure(400, character_creation.get_errors(), "Failed to create a new character. Please "
                                                                            "review the error messages provided in the"
                                                                            " response and validate the data sent.")

    def put(self):
        pass

    def delete(self):
        pass
