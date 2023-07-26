from character.domain.db_model import CharacterORM
from common.domain.module_model import ModuleModel


class Character(ModuleModel):
    id = None
    name = None
    description = None
    year_of_birth = None
    month_of_birth = None
    day_of_birth = None
    status = None
    gender = None
    life_status = None

    def __init__(self, character_id: int = None, name: str = None, description: str = None, year_of_birth: str = None,
                 month_of_birth: str = None, day_of_birth: str = None, status: str = None, gender: str = None,
                 life_status: int = None):
        super().__init__()
        self.id = character_id
        self.name = name
        self.description = description
        self.year_of_birth = year_of_birth
        self.month_of_birth = month_of_birth
        self.day_of_birth = day_of_birth
        self.status = status
        self.gender = gender
        self.life_status = life_status

    def set_by_module_orm(self, obj: CharacterORM):
        if obj.id is not None:
            self.id = obj.id

        if obj.name is not None:
            self.name = obj.name

        if obj.description is not None:
            self.description = obj.description

        if obj.year_of_birth is not None:
            self.year_of_birth = obj.year_of_birth

        if obj.month_of_birth is not None:
            self.month_of_birth = obj.month_of_birth

        if obj.day_of_birth is not None:
            self.day_of_birth = obj.day_of_birth

        if obj.status is not None:
            self.status = obj.status

        if obj.gender is not None:
            self.gender = obj.gender

        if obj.life_status is not None:
            self.life_status = obj.life_status
