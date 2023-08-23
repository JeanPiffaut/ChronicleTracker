from sqlalchemy import delete

from common.domain import Action
from milestone.domain import MilestoneORM


class Delete(Action):
    def execute(self, milestone_id):
        query = delete(MilestoneORM).where(MilestoneORM.id == milestone_id)
        try:
            result = self.session.execute(query)
            self.session.commit()
            return result.rowcount
        except Exception as err:
            self.add_error(str(err))
            return False
