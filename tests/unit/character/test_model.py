from character.domain.db_model import CharacterORM
from character.domain.model import Character


class TestCharacter:

    def test_constructor(self):
        character = Character(character_id=1, name="John Doe", year_of_birth="1985")
        assert character.id == 1
        assert character.name == "John Doe"
        assert character.year_of_birth == "1985"

    def test_validate_list(self):
        character = Character(name="John Doe", year_of_birth="1985")
        assert character._validate_length()

        character.name = "J" * 256
        assert not character._validate_length()

        character.name = "John Doe"
        character.year_of_birth = 123456789012
        assert not character._validate_length()

        character.year_of_birth = "1985"
        assert character._validate_length()

    def test_set_by_module_orm(self):
        character = Character()
        character_orm = CharacterORM(id=1, name="Jane Doe", description="Description", year_of_birth="1990")
        character.set_by_module_orm(character_orm)

        assert character.id == 1
        assert character.name == "Jane Doe"
        assert character.description == "Description"

    def test_add_error(self):
        character = Character()
        character.set_errors()
        character.add_error("Error 1")
        character.add_error("Error 2")
        assert character.get_errors() == [{'msj': "Error 1", 'type_error': Exception},
                                          {'msj': "Error 2", 'type_error': Exception}]

    def test_set_errors(self):
        character = Character()
        character.set_errors(
            [{'msj': "Error 3", 'type_error': ValueError}, {'msj': "Error 4", 'type_error': ValueError}])
        assert character.get_errors() == [{'msj': "Error 3", 'type_error': ValueError},
                                          {'msj': "Error 4", 'type_error': ValueError}]
