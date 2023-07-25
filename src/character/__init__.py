from flask import Blueprint
from flask_restful import Api

from character.interface.api_resource import ApiResource

character_bp = Blueprint('character', __name__)
api = Api(character_bp)

api.add_resource(ApiResource, '/character/<int:character_id>', endpoint='character_resource')
