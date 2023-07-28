from character.domain import Character


class Create:
    values = Character()

    def execute(self):
        self.values.validate()
