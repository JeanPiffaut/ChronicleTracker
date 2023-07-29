from database import session as default_session


class Action:
    def __init__(self, session=None):
        self._errors = dict()
        if session is not None:
            self.session = session
        else:
            self.session = default_session

    def add_error(self, error_msj: str, type_error=Exception):
        self._errors.append({'msj': error_msj, 'type_error': type_error})

    def set_errors(self, errors=list()):
        self._errors = errors

    def delete_errors(self):
        self._errors = []

    def get_errors(self):
        return self._errors

    def execute(self):
        pass
