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
        self.id = character_id
        self.name = name
        self.description = description
        self.year_of_birth = year_of_birth
        self.month_of_birth = month_of_birth
        self.day_of_birth = day_of_birth
        self.status = status
        self.gender = gender
        self.life_status = life_status

    def validate(self):
        has_error = not super(self).validate()

        if self.id is None:
            self.add_error(f'The \'id\' field cannot be None', ValueError)
            has_error = True

        if self.name is None:
            self.add_error(f'The \'name\' field cannot be None', ValueError)
            has_error = True

        if self.status is None:
            self.add_error(f'The \'status\' field cannot be None', ValueError)
            has_error = True

        if self.life_status is None:
            self.add_error(f'The \'life_status\' field cannot be None', ValueError)
            has_error = True

        return not has_error
