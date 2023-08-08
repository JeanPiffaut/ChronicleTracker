import pytest
from sqlalchemy import delete

from character.application import Create, List, Update
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
        result = create_action.execute(name=name, description=description, status=status, gender=gender,
                                       life_status=life_status)

        # Validating the result
        print(create_action.get_errors())
        assert isinstance(result, bool) and result == expectation
        query = delete(CharacterORM)
        session.execute(query)
        session.commit()

    @pytest.mark.parametrize("character_id, name, description, status, gender, life_status, expectation", test_params)
    def test_create_character_with_id(self, character_id, name, description, status, gender, life_status, expectation):
        # Mocking the session object
        create_action = Create(session)

        # Executing the action
        result = create_action.execute(character_id, name, description, status, gender, life_status)

        # Validating the result
        print(create_action.get_errors())
        assert isinstance(result, bool) and result == expectation

    @pytest.mark.parametrize("character_id, name, description, status, gender, life_status, expectation", test_params)
    def test_update_character(self, character_id, name, description, status, gender, life_status, expectation):
        # Mocking the session object
        update_action = Update(session, strict_value=False)  # You can set strict_value to True if needed
        if type(name) is str:
            name += 'a'
        elif type(name) is int:
            name = str(name + 1)

        if type(description) is str:
            description += 'a'
        elif type(description) is int:
            description = str(description + 1)

        if type(status) is str:
            status += 'a'
        elif type(status) is int:
            status = str(status + 1)

        if type(gender) is str:
            gender += 'a'
        elif type(gender) is int:
            gender = str(gender + 1)

        if type(life_status) is str:
            life_status += 'a'
        elif type(life_status) is int:
            life_status += 1

        # Executing the action
        result = update_action.execute(character_id, name, description, status, gender, life_status)

        # Validating the result
        print(update_action.get_errors())
        assert isinstance(result, bool) and result == expectation
        if expectation is not False:
            # Retrieve the updated character data from the database
            character_list = List(update_action.session)
            character_list.fill.id = character_id
            character_data = character_list.execute()
            updated_character = character_data[0]

            # Assert that the updated character's attributes match the expected values
            assert updated_character['id'] == character_id
            assert updated_character['name'] == name
            assert updated_character['description'] == description
            assert updated_character['status'] == status
            assert updated_character['gender'] == gender
            assert updated_character['life_status'] == life_status

    @pytest.mark.parametrize("character_id, name, description, status, gender, life_status, expectation", test_params)
    def test_update_character_strict(self, character_id, name, description, status, gender, life_status, expectation):
        # Mocking the session object
        update_action = Update(session, strict_value=True)  # You can set strict_value to True if needed
        if type(name) is str:
            name += 'a'
        elif type(name) is int:
            name = str(name + 1)

        if type(description) is str:
            description += 'a'
        elif type(description) is int:
            description = str(description + 1)

        if type(status) is str:
            status += 'a'
        elif type(status) is int:
            status = str(status + 1)

        if type(gender) is str:
            gender += 'a'
        elif type(gender) is int:
            gender = str(gender + 1)

        if type(life_status) is str:
            life_status += 'a'
        elif type(life_status) is int:
            life_status += 1

        # Executing the action
        result = update_action.execute(character_id, name, description, status, gender, life_status)

        # Validating the result
        print(update_action.get_errors())
        assert isinstance(result, bool) and result == expectation
        if expectation is not False:
            # Retrieve the updated character data from the database
            character_list = List(update_action.session)
            character_list.fill.id = character_id
            character_data = character_list.execute()
            updated_character = character_data[0]

            # Assert that the updated character's attributes match the expected values
            assert updated_character['id'] == character_id
            assert updated_character['name'] == name
            assert updated_character['description'] == description
            assert updated_character['status'] == status
            assert updated_character['gender'] == gender
            assert updated_character['life_status'] == life_status

    @pytest.mark.parametrize("character_id, name, description, status, gender, life_status, expectation", test_params)
    def test_list_characters_by_id(self, character_id, name, description, status, gender, life_status, expectation):
        character_orm = CharacterORM(id=character_id, name=name, description=description, status=status, gender=gender,
                                     life_status=life_status)
        # Creating and setting the parameters
        list_action = List(session)
        list_action.fill.id = character_id

        # Executing the action
        result = list_action.execute()
        print(list_action.get_errors())

        # Validating the result
        assert (len(result) >= 1) == expectation

    def test_clean_bd(self):
        query = delete(CharacterORM)
        session.execute(query)
        session.commit()
