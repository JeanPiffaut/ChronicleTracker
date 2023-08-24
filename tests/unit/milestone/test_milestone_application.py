from datetime import datetime, timedelta

import pytest
from sqlalchemy import delete

from milestone.application import Create, Update, List, Delete
from milestone.domain import Milestone, MilestoneORM
from unit.database import session
from unit.milestone import test_params


class TestMilestoneApplication:
    @pytest.mark.parametrize("milestone_id, description, date, expectation", test_params)
    def test_validate_create(self, milestone_id, description, date, expectation):
        if milestone_id is not None:
            milestone_id = str(milestone_id)

        if description is not None:
            description = str(description)

        if date is not None and type(date) is str:
            date = datetime.fromisoformat(date)

        milestone = Milestone(milestone_id=milestone_id, description=description, date=date)
        result = milestone.validate_create()

        print(milestone.get_errors())
        assert isinstance(result, bool) and result == expectation

    @pytest.mark.parametrize("milestone_id, description, date, expectation", test_params)
    def test_create_milestone(self, milestone_id, description, date, expectation):
        # Mocking the session object
        create_action = Create(session)

        # Executing the action
        result = create_action.execute(description=description, date=date)

        print(create_action.get_errors())
        # Validating the result
        assert isinstance(result, bool) and result == expectation
        delete_query = delete(MilestoneORM)
        session.execute(delete_query)
        session.commit()

    @pytest.mark.parametrize("milestone_id, description, date, expectation", test_params)
    def test_create_milestone_with_id(self, milestone_id, description, date, expectation):
        # Mocking the session object
        create_action = Create(session)

        # Executing the action
        result = create_action.execute(milestone_id=milestone_id, description=description, date=date)
        print(create_action.get_errors())

        # Validating the result
        assert isinstance(result, bool) and result == expectation

    @pytest.mark.parametrize("milestone_id, description, date, expectation", test_params)
    def test_update_milestone(self, milestone_id, description, date, expectation):
        # Mocking the session object
        update_action = Update(session, strict_value=False)
        if type(description) is str:
            description += 'a'
        elif type(description) is int:
            description = str(description + 1)

        if date is not None and type(date) is datetime:
            date += timedelta(days=1)

        # Executing the action
        result = update_action.execute(milestone_id=milestone_id, description=description, date=date)
        print(update_action.get_errors())

        # Validating the result
        assert isinstance(result, bool) and result == expectation

        if expectation is not False:
            # Retrieve the updated milestone data from the database
            milestone_list = List(update_action.session)
            milestone_list.fill.id = milestone_id
            milestone_data = milestone_list.execute()
            updated_milestone = milestone_data[0]

            # Assert that the updated milestone's attributes match the expected values
            assert updated_milestone['id'] == milestone_id
            assert updated_milestone['description'] == description
            if date is not None and type(date) is str:
                assert updated_milestone['date'].strftime("%Y-%m-%d") == datetime.fromisoformat(date).strftime(
                    "%Y-%m-%d")
            elif date is not None and type(date) is datetime:
                assert updated_milestone['date'].strftime("%Y-%m-%d") == date.strftime("%Y-%m-%d")

    import pytest

    @pytest.mark.parametrize("milestone_id, description, date, expectation", test_params)
    def test_delete_milestone(self, milestone_id, description, date, expectation):
        # Eliminar todos los elementos existentes antes de comenzar la prueba
        delete_all_query = delete(MilestoneORM)
        session.execute(delete_all_query)
        session.commit()

        # Crear un hito para ser eliminado (esta parte es similar a tu prueba de creación)
        create_action = Create(session)
        create_result = create_action.execute(description=description, date=date)
        assert isinstance(create_result, bool) and create_result == expectation
        if create_result is not False:
            # Ejecutar la acción (eliminar el hito)
            delete_action = Delete(session)
            delete_result = delete_action.execute(create_action.milestone_created['id'])

            # Validar el resultado
            assert isinstance(delete_result, int) and delete_result >= 0
            if expectation:
                assert delete_result == 1
            else:
                assert delete_result == 0

        # Limpiar: deshacer y cerrar la sesión
        session.rollback()
        session.close()
