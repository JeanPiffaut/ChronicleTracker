from character.domain import Character
from common.domain import Action


class Update(Action):
    def execute(self, character_id=None, name=None, description=None, status=None, gender=None, life_status=None):
        if name is not None:
            name = str(name)

        if description is not None:
            description = str(description)

        if status is not None:
            status = str(status)

        if gender is not None:
            gender = str(gender)

        character = Character(character_id=character_id, name=name, description=description, status=status,
                              gender=gender, life_status=life_status)
        if character.validate_create() is False:
            errors = character.get_errors()
            self.set_errors(errors)
            return False
