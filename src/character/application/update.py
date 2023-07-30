from sqlalchemy import update

from character.domain import CharacterORM
from common.domain import Action


class Update(Action):

    def __init__(self, session=None, strict_value=False):
        super().__init__(session)
        self.strict_value = strict_value

    def execute(self, character_id=None, name=None, description=None, status=None, gender=None, life_status=None):
        if self.strict_value:
            query = update(CharacterORM).values(name=name, description=description, status=status, gender=gender,
                                                life_status=life_status).where(CharacterORM.id == character_id)
        else:
            query = update(CharacterORM).where(CharacterORM.id == character_id)
            if name is not None:
                query = query.values(name=name)
            if description is not None:
                query = query.values(description=description)
            if status is not None:
                query = query.values(status=status)
            if gender is not None:
                query = query.values(gender=gender)
            if life_status is not None:
                query = query.values(life_status=life_status)

        try:
            result = self.session.execute(query)
            self.session.commit()
            return bool(result.rowcount)
        except Exception as err:
            self.add_error(str(err))
            return False
