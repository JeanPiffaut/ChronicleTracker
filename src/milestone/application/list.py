from common.domain import Action
from milestone.domain import Milestone


class List(Action):
    def __init__(self, session=None):
        super().__init__(session)
        self.fill = Milestone()

    def execute(self):
        pass
