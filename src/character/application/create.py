from character.domain import Character, CharacterORM
from common.domain import Action
from sqlalchemy import insert


class Create(Action):

    def execute(self, name=None, description=None, status=None, gender=None, life_status=None):
        if name is not None:
            name = str(name)

        if description is not None:
            description = str(description)

        if status is not None:
            status = str(status)

        if gender is not None:
            gender = str(gender)

        character = Character(name=name, description=description, status=status, gender=gender, life_status=life_status)
        character.sanitize_for_mysql()
        if character.validate_create() is False:
            errors = character.get_errors()
            self.set_errors(errors)
            return False

        query = insert(CharacterORM).values(name=character.name, description=character.description,
                                            status=character.status, gender=character.gender,
                                            life_status=character.life_status)
        result = self.session.execute(query)
        self.session.commit()
        return bool(result.rowcount)
