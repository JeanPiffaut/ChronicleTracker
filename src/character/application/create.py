from character.domain import Character, CharacterORM
from common.domain import Action
from sqlalchemy import insert


class Create(Action):
    values = Character()

    def execute(self):
        self.values.sanitize_for_mysql()
        if self.values.validate_create() is False:
            errors = self.values.get_errors()
            self.set_errors(errors)
            return False

        query = insert(CharacterORM).values(name=self.values.name, description=self.values.description,status=self.values.status,
                                            gender=self.values.gender, life_status=self.values.life_status)
        result = self.session.execute(query)
        self.session.commit()
        return bool(result.rowcount)
