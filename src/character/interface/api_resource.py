from flask import request, jsonify
from flask_restful import Resource

from character.application import List, Create, Update
from common.misc import response_structure
from database import session


class ApiResource(Resource):
    def get(self, character_id=None):
        character_list = List(session)
        if character_id is not None:
            character_list.fill.id = character_id

        if request.is_json is not None:
            args = request.get_json()
            character_list.fill.name = args.get('name', None)
            character_list.fill.description = args.get('description', None)
            character_list.fill.status = args.get('status', None)
            character_list.fill.gender = args.get('gender', None)
            character_list.fill.life_status = args.get('life_status', None)

        response = character_list.execute()
        if response is not False:
            return response_structure(200, response)
        else:
            errors = character_list.get_errors()
            return response_structure(400, errors)

    def post(self):
        args = request.get_json()
        character_creation = Create(session)
        result = character_creation.execute(name=args.get('name'), description=args.get('description', None),
                                            status=args.get('status'), gender=args.get('gender', None),
                                            life_status=args.get('life_status'))
        if result:
            return response_structure(201)
        else:
            return response_structure(400, character_creation.get_errors(), "Failed to create a new character. Please "
                                                                            "review the error messages provided in the"
                                                                            " response and validate the data sent.")

    def put(self, character_id):
        return self._update_character(True, character_id)

    def patch(self, character_id):
        return self._update_character(False, character_id)

    def delete(self, character_id):
        pass

    def _update_character(self, strict, character_id):
        args = request.get_json()
        update_character = Update(session, strict)
        result = update_character.execute(character_id, str(args.get('name')), str(args.get('description')),
                                          str(args.get('status')), str(args.get('gender')),
                                          str(args.get('life_status')))
        if result:
            return response_structure(200)
        else:
            return response_structure(400, update_character.get_errors())
