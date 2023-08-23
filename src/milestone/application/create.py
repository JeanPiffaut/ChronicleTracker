from datetime import datetime

from sqlalchemy import insert

from common.domain import Action
from milestone.application import List
from milestone.domain import Milestone, MilestoneORM


class Create(Action):
    def __init__(self, session=None):
        super().__init__(session)
        self.milestone_created = None

    def execute(self, milestone_id=None, description=None, date=None):
        if milestone_id is not None:
            milestone_id = str(milestone_id)

        if description is not None:
            description = str(description)

        if date is not None:
            date = datetime.fromisoformat(date)

        milestone = Milestone(milestone_id=milestone_id, description=description, date=date)
        if milestone.validate_create() is False:
            errors = milestone.get_errors()
            self.set_errors(errors)
            return False

        query = insert(MilestoneORM).values(id=milestone.id, description=milestone.description,
                                            date=milestone.date)
        try:
            result = self.session.execute(query)
            self.session.commit()
            milestone_list = List(self.session)
            milestone_list.fill.id = result.lastrowid
            character_data = milestone_list.execute()
            self.milestone_created = character_data[0]
            return True
        except Exception as err:
            self.add_error(err.__str__())
            return False
