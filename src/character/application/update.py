from sqlalchemy import update

from character.application import List
from character.domain import CharacterORM, Character
from common.domain import Action


class Update(Action):

    def __init__(self, session=None, strict_value=False):
        super().__init__(session)
        self.character_updated = None
        self.strict_value = strict_value

    def execute(self, character_id=None, name=None, description=None, status=None, gender=None, life_status=None):
        if self.strict_value:
            if name == 'None':
                name = None

            if description == 'None':
                description = None

            if status == 'None':
                status = None

            if gender == 'None':
                gender = None

            if life_status == 'None':
                life_status = None
            character = Character(character_id=character_id, name=name, description=description, status=status,
                                  gender=gender, life_status=life_status)
            if character.validate_create() is False:
                errors = character.get_errors()
                self.set_errors(errors)
                return False
            query = update(CharacterORM).values(name=character.name, description=character.description,
                                                status=character.status, gender=character.gender,
                                                life_status=character.life_status).where(
                CharacterORM.id == character_id)
        else:
            character = Character(character_id=character_id, name=name, description=description, status=status,
                                  gender=gender, life_status=life_status)
            if character.validate_create() is False:
                errors = character.get_errors()
                self.set_errors(errors)
                return False

            query = update(CharacterORM).where(CharacterORM.id == character_id)
            if character.name is not None and character.name != 'None':
                query = query.values(name=character.name)
            if character.description is not None and character.description != 'None':
                query = query.values(description=character.description)
            if character.status is not None and character.status != 'None':
                query = query.values(status=character.status)
            if character.gender is not None and character.gender != 'None':
                query = query.values(gender=character.gender)
            if character.life_status is not None and character.life_status != 'None':
                query = query.values(life_status=character.life_status)

        try:
            result = self.session.execute(query)
            self.session.commit()
            character_list = List(self.session)
            character_list.fill.id = character_id
            character_data = character_list.execute()
            self.character_updated = character_data[0]
            return bool(result.rowcount)
        except Exception as err:
            self.add_error(str(err))
            return False
