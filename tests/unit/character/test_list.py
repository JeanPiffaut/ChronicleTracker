import pytest
from character.application import List
from character.domain import CharacterORM
from unittest.mock import MagicMock

from unit.character import test_params
from unit.database import session


class TestListAction:
    # Test cases for List action class
    @pytest.mark.parametrize("name, description, status, gender, life_status, expectation", test_params)
    def test_list_characters(self, name, description, status, gender, life_status, expectation):
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
