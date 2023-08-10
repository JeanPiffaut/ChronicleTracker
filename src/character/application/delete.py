from sqlalchemy import delete

from character.domain import CharacterORM
from common.domain import Action


class Delete(Action):

    def execute(self, character_id):
        query = delete(CharacterORM).where(CharacterORM.id == character_id)
        try:
            result = self.session.execute(query)
            self.session.commit()
            return result.rowcount
        except Exception as err:
            self.add_error(str(err))
            return False
