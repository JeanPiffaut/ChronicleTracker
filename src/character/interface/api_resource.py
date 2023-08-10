from flask import request, jsonify
from flask_restful import Resource

from character.application import List, Create, Update, Delete
from common.misc import response_structure
from database import session


class ApiResource(Resource):
    def get(self, character_id=None):
        list_obj = List(session)
        if character_id is not None:
            list_obj.fill.id = character_id
        elif request.is_json is not None:
            args = request.get_json()
            list_obj.fill.name = args.get('name', None)
            list_obj.fill.description = args.get('description', None)
            list_obj.fill.status = args.get('status', None)
            list_obj.fill.gender = args.get('gender', None)
            list_obj.fill.life_status = args.get('life_status', None)

        response = list_obj.execute()
        if type(response) is list and len(response) > 0:
            if character_id is not None:
                character = response[0]
                return response_structure(200, character)
            else:
                return response_structure(200, response)

        elif type(response) is list and len(response) is 0:
            return response_structure(404, message='Character not found.')
        else:
            return response_structure(400, list_obj.get_errors(), 'Bad request')

    def post(self):
        args = request.get_json()
        creation_obj = Create(session)
        result = creation_obj.execute(name=args.get('name'), description=args.get('description', None),
                                      status=args.get('status'), gender=args.get('gender', None),
                                      life_status=args.get('life_status'))
        if result:
            return response_structure(201, creation_obj.character_created, 'Character created successfully')
        else:
            return response_structure(400, creation_obj.get_errors(), "Bad request")

    def put(self, character_id):
        return self._update_character(True, character_id)

    def patch(self, character_id):
        return self._update_character(False, character_id)

    def delete(self, character_id):
        delete_obj = Delete(session)
        result = delete_obj.execute(character_id)
        if type(result) is int and result == 1:
            return response_structure(204, message='Character deleted successfully')
        elif type(result) is int and result == 0:
            return response_structure(404, message='Character not found')
        else:
            return response_structure(400, delete_obj.get_errors(), 'Bad request')

    def _update_character(self, strict, character_id):
        args = request.get_json()
        update_obj = Update(session, strict)
        result = update_obj.execute(character_id, str(args.get('name')), str(args.get('description')),
                                    str(args.get('status')), str(args.get('gender')),
                                    str(args.get('life_status')))
        if result:
            return response_structure(200, update_obj.character_updated, 'Character updated successfully')
        else:
            return response_structure(400, update_obj.get_errors(), 'Bad request')
