import pytest

from character.application import Create, List
from character.domain import Character, CharacterORM
from unit.character import test_params
from unit.database import session


class TestCharacterApplication:
    @pytest.mark.parametrize("character_id, name, description, status, gender, life_status, expectation", test_params)
    def test_validate_create(self, character_id, name, description, status, gender, life_status, expectation):
        if name is not None:
            name = str(name)

        if description is not None:
            description = str(description)

        if status is not None:
            status = str(status)

        if gender is not None:
            gender = str(gender)

        character = Character(name=name, description=description, status=status, gender=gender, life_status=life_status)
        result = character.validate_create()

        print(character.get_errors())
        # Validating the result
        assert isinstance(result, bool) and result == expectation

    @pytest.mark.parametrize("character_id, name, description, status, gender, life_status, expectation", test_params)
    def test_create_character(self, character_id, name, description, status, gender, life_status, expectation):
        # Mocking the session object
        create_action = Create(session)

        # Executing the action
        result = create_action.execute(character_id, name, description, status, gender, life_status)

        # Validating the result
        print(create_action.get_errors())
        assert isinstance(result, bool) and result == expectation

    @pytest.mark.parametrize("character_id, name, description, status, gender, life_status, expectation", test_params)
    def test_list_characters_by_id(self, character_id, name, description, status, gender, life_status, expectation):
        character_orm = CharacterORM(id=character_id, name=name, description=description, status=status, gender=gender,
                                     life_status=life_status)
        # Creating and setting the parameters
        list_action = List(session)
        list_action.fill.id = character_id

        # Executing the action
        result = list_action.execute()
        print(result)
        # Validating the result
        assert (len(result) >= 1) == expectation
