from character.application.list import List
from character.domain.model import Character
from unit.database import session, engine


class TestList:

    def test_execute_valid(self):
        # Creamos un objeto de Character con datos válidos para la prueba
        character = Character(character_id=1, name="John Doe", year_of_birth="1985")

        # Creamos un objeto List para la prueba
        list_obj = List(session)
        list_obj.fill = character

        # Ejecutamos el método execute y verificamos los resultados
        result = list_obj.execute()
        assert result[0]['id'] == character.id

    def test_execute_invalid(self):
        # Creamos un objeto de Character con datos inválidos para la prueba
        character = Character(character_id=1, name="J" * 256, year_of_birth="1985")

        # Creamos un objeto List para la prueba
        list_obj = List(session)
        list_obj.fill = character

        # Ejecutamos el método execute y verificamos que retorne False (indicando que hubo errores)
        result = list_obj.execute()
        assert result is False

        # Verificamos que se hayan agregado errores a la lista de errores del objeto List
        assert list_obj.get_errors() == [
            {'msj': "The 'name' field cannot exceed 255 characters", 'type_error': ValueError}]
