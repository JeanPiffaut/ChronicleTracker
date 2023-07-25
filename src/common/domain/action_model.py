class Action:
    _errors = []

    def add_error(self, error_msj: str, type_error=Exception):
        self._errors.append({'msj': error_msj, 'type_error': type_error})

    def set_errors(self, errors=[]):
        self._errors = errors

    def get_errors(self):
        return self._errors

    def execute(self):
        pass
