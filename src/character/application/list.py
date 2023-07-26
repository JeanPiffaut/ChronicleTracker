from sqlalchemy import select
from character.domain.db_model import CharacterORM
from character.domain.model import Character
from common.domain.action_model import Action


class List(Action):
    fill = Character()

    def execute(self):
        fill_params = self.fill
        if fill_params.validate_list() is False:
            errors = fill_params.get_errors()
            self.set_errors(errors)
            return False

        query = select(CharacterORM)
        if fill_params.id is not None:
            query = query.where(CharacterORM.id == fill_params.id)

        result = self.session.execute(query)
        user_list = []
        for user_obj in result.scalars():
            char = Character()
            char.set_by_module_orm(user_obj)
            user_list.append(char.__dict__)

        return user_list
