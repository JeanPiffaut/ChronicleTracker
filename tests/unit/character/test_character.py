import pytest

from character.application import Create, List
from character.domain import Character, CharacterORM
from unit.character import test_params
from unit.database import session


class TestCharacter:
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
        result = create_action.execute(name, description, status, gender, life_status)

        # Validating the result
        print(create_action.get_errors())
        assert isinstance(result, bool) and result == expectation

    @pytest.mark.parametrize("character_id, name, description, status, gender, life_status, expectation", test_params)
    def test_list_characters(self, character_id, name, description, status, gender, life_status, expectation):
        character_orm = CharacterORM(name=name, description=description, status=status, gender=gender,
                                     life_status=life_status)
        # Creating and setting the parameters
        list_action = List(session)
        list_action.fill.name = name
        list_action.fill.description = description
        list_action.fill.status = status
        list_action.fill.gender = gender
        list_action.fill.life_status = life_status

        # Executing the action
        result = list_action.execute()

        # Validating the result
        if expectation:
            assert isinstance(result, list)
            assert len(result) == 1
            assert result[0]['id'] == character_orm.id
            assert result[0]['name'] == character_orm.name
            assert result[0]['description'] == character_orm.description
            assert result[0]['status'] == character_orm.status
            assert result[0]['gender'] == character_orm.gender
            assert result[0]['life_status'] == character_orm.life_status
            assert not list_action.get_errors()  # No error messages should be present on success
        else:
            assert not result  # The result list should be empty when there are no matching records
