import pytest
from character.application import Create
from character.domain import Character
from unit.character import test_params
from unit.database import session


class TestCreateAction:
    # Test cases for Create action class
    @pytest.mark.parametrize("name, description, status, gender, life_status, expectation", test_params)
    def test_create_character(self, name, description, status, gender, life_status, expectation):
        # Mocking the session object
        create_action = Create(session)

        # Setting the values
        create_action.values.name = name
        create_action.values.description = description
        create_action.values.status = status
        create_action.values.gender = gender
        create_action.values.life_status = life_status

        # Executing the action
        result = create_action.execute()

        # Validating the result
        assert isinstance(result, bool) and result == expectation


class TestCharacterModel:
    # Test cases for Character model
    @pytest.mark.parametrize("name, description, status, gender, life_status, expectation", test_params)
    def test_validate_create(self, name, description, status, gender, life_status, expectation):
        character = Character(name=name, description=description, status=status, gender=gender, life_status=life_status)
        result = character.validate_create()

        # Validating the result
        assert isinstance(result, bool) and result == expectation

# Add more test cases as needed to cover different scenarios.
