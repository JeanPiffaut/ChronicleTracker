from character.domain.db_model import CharacterORM
from common.domain.module_model import ModuleModel


class Character(ModuleModel):
    def __init__(self, character_id: int = None, name: str = None, description: str = None, status: str = None,
                 gender: str = None, life_status: int = None):
        super().__init__()
        if type(character_id).__name__ == "int":
            self.id = character_id
        else:
            self.id = None
        self.name = name
        self.description = description
        self.status = status
        self.gender = gender
        if type(life_status).__name__ == "int":
            self.life_status = life_status
        else:
            self.life_status = None

    def set_by_module_orm(self, obj: CharacterORM):
        if obj.id is not None:
            self.id = obj.id

        if obj.name is not None:
            self.name = obj.name

        if obj.description is not None:
            self.description = obj.description

        if obj.status is not None:
            self.status = obj.status

        if obj.gender is not None:
            self.gender = obj.gender

        if obj.life_status is not None:
            self.life_status = obj.life_status

    def validate_create(self):
        has_error = not super().validate()
        if self.name is None or self.name.strip() == "":
            self.add_error(f'The \'name\' field cannot be None or Empty', ValueError)
            has_error = True

        if self.status is None or self.status.strip() == "":
            self.add_error(f'The \'status\' field cannot be None or Empty', ValueError)
            has_error = True

        if self.life_status is None or self.life_status == "":
            self.add_error(f'The \'life_status\' field cannot be None or Empty', ValueError)
            has_error = True

        return not has_error
