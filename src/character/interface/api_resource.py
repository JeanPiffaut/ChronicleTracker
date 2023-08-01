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
        if type(response) is list and len(response) > 0:
            if character_id is not None:
                character = response[0]
                return response_structure(200, character)
            else:
                return response_structure(200, response)

        elif type(response) is list and len(response) is 0:
            return response_structure(404, message='Character not found.')
        else:
            return response_structure(400, character_list.get_errors(), 'Bad request')

    def post(self):
        args = request.get_json()
        character_creation = Create(session)
        result = character_creation.execute(name=args.get('name'), description=args.get('description', None),
                                            status=args.get('status'), gender=args.get('gender', None),
                                            life_status=args.get('life_status'))
        if result:
            return response_structure(201, message='Character created successfully')
        else:
            return response_structure(400, character_creation.get_errors(), "Bad request")

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
            return response_structure(200, message='Character updated successfully')
        else:
            return response_structure(400, update_character.get_errors(), 'Bad request')
