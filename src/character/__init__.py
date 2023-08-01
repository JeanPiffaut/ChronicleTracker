from flask import Blueprint
from flask_restful import Api

from character.interface import ApiResource

character_bp = Blueprint('character', __name__)
api = Api(character_bp)

api.add_resource(ApiResource, '/character', endpoint='character_resource', methods=['POST', 'GET'])
api.add_resource(ApiResource, '/character/<int:character_id>', endpoint='character_resource_by_id',
                 methods=['GET', 'PUT', 'PATCH', 'DELETE'])
