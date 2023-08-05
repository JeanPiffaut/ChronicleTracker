from select import select

from character.application import List
from character.domain import Character, CharacterORM
from common.domain import Action
from sqlalchemy import insert


class Create(Action):

    def __init__(self, session=None):
        super().__init__(session)
        self.character_created = None

    def execute(self, character_id=None, name=None, description=None, status=None, gender=None, life_status=None):
        if name is not None:
            name = str(name)

        if description is not None:
            description = str(description)

        if status is not None:
            status = str(status)

        if gender is not None:
            gender = str(gender)

        character = Character(character_id=character_id, name=name, description=description, status=status, gender=gender, life_status=life_status)
        if character.validate_create() is False:
            errors = character.get_errors()
            self.set_errors(errors)
            return False

        query = insert(CharacterORM).values(id=character.id, name=character.name, description=character.description,
                                            status=character.status, gender=character.gender,
                                            life_status=character.life_status)
        try:
            result = self.session.execute(query)
            self.session.commit()
            character_list = List(self.session)
            character_list.fill.id = result.lastrowid
            character_data = character_list.execute()
            self.character_created = character_data[0]
            return True
        except Exception as err:
            print(1)
            self.add_error(err.__str__())
            return False


