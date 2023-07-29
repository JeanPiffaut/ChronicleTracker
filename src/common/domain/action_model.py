class Action:
    def __init__(self, session=None):
        self.errors = list()
        self.session = session

    def add_error(self, error_msj: str, type_error=Exception):
        self.errors.append({'msj': error_msj, 'type_error': type_error})

    def set_errors(self, errors=list()):
        self.errors = errors

    def delete_errors(self):
        self.errors = []

    def get_errors(self):
        return self.errors

    def execute(self):
        pass
