from sqlalchemy import select
from common.domain import Action
from milestone.domain import Milestone, MilestoneORM


class List(Action):
    def __init__(self, session=None):
        super().__init__(session)
        self.fill = Milestone()

    def execute(self):
        fill_params = self.fill
        if fill_params.validate() is False:
            errors = fill_params.get_errors()
            self.set_errors(errors)
            return False

        query = select(MilestoneORM)
        if fill_params.id is not None:
            query = query.where(MilestoneORM.id == fill_params.id)

        if fill_params.description is not None:
            query = query.where(MilestoneORM.description == fill_params.description)

        if fill_params.date is not None:
            query = query.where(MilestoneORM.date == fill_params.date)

        result = self.session.execute(query)

        milestone_list = list()
        for milestone_obj in result.scalars():
            char = Milestone()
            char.set_by_module_orm(milestone_obj)
            milestone_list.append(char.to_dict())

        return milestone_list
