from sqlalchemy import update

from character.application import List
from character.domain import CharacterORM
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
            query = update(CharacterORM).values(name=name, description=description, status=status, gender=gender,
                                                life_status=life_status).where(CharacterORM.id == character_id)
        else:
            query = update(CharacterORM).where(CharacterORM.id == character_id)
            if name is not None and name != 'None':
                query = query.values(name=name)
            if description is not None and description != 'None':
                query = query.values(description=description)
            if status is not None and status != 'None':
                query = query.values(status=status)
            if gender is not None and gender != 'None':
                query = query.values(gender=gender)
            if life_status is not None and life_status != 'None':
                query = query.values(life_status=life_status)

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
