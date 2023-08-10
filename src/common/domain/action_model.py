class Action:
    def __init__(self, session=None):
        self.errors = list()
        self.session = session

    def add_error(self, error_msj: str):
        self.errors.append(error_msj)

    def set_errors(self, errors=None):
        if errors is None:
            errors = list()
        self.errors = errors

    def delete_errors(self):
        self.errors = []

    def get_errors(self):
        return self.errors

    def execute(self):
        pass
