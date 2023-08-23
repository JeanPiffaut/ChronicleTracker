from sqlalchemy import select
from character.domain import CharacterORM
from character.domain import Character
from common.domain import Action


class List(Action):
    def __init__(self, session=None):
        super().__init__(session)
        self.fill = Character()

    def execute(self):
        fill_params = self.fill
        if fill_params.validate() is False:
            errors = fill_params.get_errors()
            self.set_errors(errors)
            return False

        query = select(CharacterORM)
        if fill_params.id is not None:
            query = query.where(CharacterORM.id == fill_params.id)

        if fill_params.name is not None:
            query = query.where(CharacterORM.name == fill_params.name)

        if fill_params.description is not None:
            query = query.where(CharacterORM.description == fill_params.description)

        if fill_params.status is not None:
            query = query.where(CharacterORM.status == fill_params.status)

        if fill_params.gender is not None:
            query = query.where(CharacterORM.gender == fill_params.gender)

        if fill_params.life_status is not None:
            query = query.where(CharacterORM.life_status == fill_params.life_status)

        result = self.session.execute(query)

        character_list = list()
        for character_obj in result.scalars():
            char = Character()
            char.set_by_module_orm(character_obj)
            character_list.append(char.to_dict())

        return character_list
