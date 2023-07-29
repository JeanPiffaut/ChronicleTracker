import pytest
from character.application import Create
from character.domain import Character
from unit.character import test_params
from unit.database import session


class TestCreateAction:
    # Test cases for Create action class
    @pytest.mark.parametrize("character_id, name, description, status, gender, life_status, expectation", test_params)
    def test_create_character(self, character_id, name, description, status, gender, life_status, expectation):
        # Mocking the session object
        create_action = Create(session)

        # Executing the action
        result = create_action.execute(name, description, status, gender, life_status)

        # Validating the result
        print(create_action.get_errors())
        assert isinstance(result, bool) and result == expectation

# Add more test cases as needed to cover different scenarios.
