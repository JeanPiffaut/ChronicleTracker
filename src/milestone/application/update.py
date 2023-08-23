from sqlalchemy import update

from common.domain import Action
from milestone.application import List
from milestone.domain import Milestone, MilestoneORM


class Update(Action):
    def __init__(self, session=None, strict_value=False):
        super().__init__(session)
        self.milestone_updated = None
        self.strict_value = strict_value

    def execute(self, milestone_id=None, description=None, date=None):
        if self.strict_value:
            if milestone_id == 'None':
                milestone_id = None

            if description == 'None':
                description = None

            if date == 'None':
                date = None

            milestone = Milestone(milestone_id=milestone_id, description=description, date=date)
            if milestone.validate_create() is False:
                errors = milestone.get_errors()
                self.set_errors(errors)
                return False
            query = update(MilestoneORM).values(id=milestone.id, description=milestone.description,
                                                date=milestone.date).where(
                MilestoneORM.id == milestone_id)
        else:
            milestone = Milestone(milestone_id=milestone_id, description=description, date=date)
            if milestone.validate_create() is False:
                errors = milestone.get_errors()
                self.set_errors(errors)
                return False

            query = update(MilestoneORM).where(MilestoneORM.id == milestone_id)
            if milestone.id is not None and milestone.id != 'None':
                query = query.values(id=milestone.id)
            if milestone.description is not None and milestone.description != 'None':
                query = query.values(description=milestone.description)
            if milestone.date is not None and milestone.date != 'None':
                query = query.values(date=milestone.date)

        try:
            result = self.session.execute(query)
            self.session.commit()
            character_list = List(self.session)
            character_list.fill.id = milestone_id
            character_data = character_list.execute()
            self.milestone_updated = character_data[0]
            return bool(result.rowcount)
        except Exception as err:
            self.add_error(str(err))
            return False
