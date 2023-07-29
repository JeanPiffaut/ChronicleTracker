import pytest

from character.domain import Character
from unit.character import test_params


class TestCharacterModel:
    # Test cases for Character model
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
