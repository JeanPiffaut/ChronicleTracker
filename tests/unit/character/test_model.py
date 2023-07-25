from character.domain.db_model import CharacterORM
from character.domain.model import Character
from common.domain.module_model import ModuleModel


# Pruebas para la clase Character
class TestCharacter:

    def test_constructor(self):
        character = Character(character_id=1, name="John Doe", year_of_birth="1985")
        assert character.id == 1
        assert character.name == "John Doe"
        assert character.year_of_birth == "1985"

    def test_validate_list(self):
        character = Character(name="John Doe", year_of_birth="1985")
        assert not character.validate_list()  # Debe retornar False ya que no hay errores

        character.name = "J" * 256  # Nombre con demasiados caracteres
        assert character.validate_list()  # Debe retornar True ya que hay un error

        character.name = "John Doe"
        character.year_of_birth = 123456789012  # Año de nacimiento con demasiados caracteres
        assert character.validate_list()  # Debe retornar True ya que hay un error

        character.year_of_birth = "1985"
        assert not character.validate_list()  # Debe retornar False ya que no hay errores

    def test_set_by_module_orm(self):
        character = Character()
        character_orm = CharacterORM(id=1, name="Jane Doe", description="Description", year_of_birth="1990")
        character.set_by_module_orm(character_orm)

        assert character.id == 1
        assert character.name == "Jane Doe"
        assert character.description == "Description"
        assert character.year_of_birth == "1990"
