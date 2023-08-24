from flask import request
from flask_restful import Resource

from common.misc import response_structure
from database import session
from milestone.application import List, Create, Update, Delete


class ApiResource(Resource):
    def get(self, character_id=None):
        list_obj = List(session)
        if character_id is not None:
            list_obj.fill.id = character_id
        elif request.is_json is not None:
            args = request.get_json()
            list_obj.fill.name = args.get('id', None)
            list_obj.fill.description = args.get('description', None)
            list_obj.fill.status = args.get('date', None)

        response = list_obj.execute()
        if type(response) is list and len(response) > 0:
            if character_id is not None:
                character = response[0]
                return response_structure(200, character)
            else:
                return response_structure(200, response)

        elif type(response) is list and len(response) is 0:
            return response_structure(404, message='Milestone not found.')
        else:
            return response_structure(400, list_obj.get_errors(), 'Bad request')

    def post(self):
        args = request.get_json()
        creation_obj = Create(session)
        result = creation_obj.execute(milestone_id=args.get('id'), description=args.get('description'),
                                      date=args.get('date'))
        if result:
            return response_structure(201, creation_obj.milestone_created, 'Milestone created successfully')
        else:
            return response_structure(400, creation_obj.get_errors(), "Bad request")

    def put(self, milestone_id):
        return self._update_milestone(True, milestone_id)

    def patch(self, milestone_id):
        return self._update_milestone(False, milestone_id)

    def delete(self, milestone_id):
        delete_obj = Delete(session)
        result = delete_obj.execute(milestone_id)
        if type(result) is int and result == 1:
            return response_structure(204, message='Milestone deleted successfully')
        elif type(result) is int and result == 0:
            return response_structure(404, message='Milestone not found')
        else:
            return response_structure(400, delete_obj.get_errors(), 'Bad request')

    def _update_milestone(self, strict, character_id):
        args = request.get_json()
        update_obj = Update(session, strict)
        result = update_obj.execute(character_id, str(args.get('description')), str(args.get('date')))

        if result:
            return response_structure(200, update_obj.milestone_updated, 'Milestone updated successfully')
        else:
            return response_structure(400, update_obj.get_errors(), 'Bad request')
