import pytest

from character.domain import Character
from unit.character import test_params


class TestCharacterModel:
    # Test cases for Character model
    @pytest.mark.parametrize("name, description, status, gender, life_status, expectation", test_params)
    def test_validate_create(self, name, description, status, gender, life_status, expectation):
        if name is not None:
            name = str(name)

        if description is not None:
            description = str(description)

        if status is not None:
            status = str(status)

        if gender is not None:
            gender = str(gender)

        character = Character(name=name, description=description, status=status, gender=gender, life_status=life_status)
        character.set_errors()
        result = character.validate_create()

        # Validating the result
        assert isinstance(result, bool) and result == expectation
        if result is not False:
            assert not character.get_errors()
