from datetime import datetime

from common.domain import ModuleModel
from milestone.domain import MilestoneORM


class Milestone(ModuleModel):
    def __init__(self, milestone_id: int = None, description: str = None, date: datetime = None):
        super().__init__()
        self.id = milestone_id
        self.description = description
        self.date = date

    def set_by_module_orm(self, obj: MilestoneORM):
        if obj.id is not None:
            self.id = obj.id

        if obj.description is not None:
            self.description = obj.description

        if obj.date is not None:
            self.date = obj.date

    def validate_create(self):
        has_error = not super().validate()
        if self.description is None or self.description.strip() == "":
            self.add_error(f'The \'description\' field cannot be None or Empty', ValueError)
            has_error = True

        return not has_error

