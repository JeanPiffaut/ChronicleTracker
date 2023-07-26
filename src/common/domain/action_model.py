from database import session as default_session


class Action:
    session = None
    _errors = []

    def __init__(self, session=None) -> None:
        if session is not None:
            self.session = session
        else:
            self.session = default_session

    def add_error(self, error_msj: str, type_error=Exception):
        self._errors.append({'msj': error_msj, 'type_error': type_error})

    def set_errors(self, errors=[]):
        self._errors = errors

    def get_errors(self):
        return self._errors

    def execute(self):
        pass
