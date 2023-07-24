class ModuleModel:
    _errors = []

    def add_error(self, error_msj: str, type_error=Exception):
        self._errors.append({'msj': error_msj, 'type_error': type_error})

    def delete_errors(self):
        self._errors = []

    def get_errors(self):
        return self._errors

    def _validate_length(self):
        has_error = False
        params = self.__dict__
        for param, value in params.items():
            if type(value).__name__ == 'str' and len(value) >= 255:
                self.add_error(f'The \'{param}\' field cannot exceed 255 characters', ValueError)
                has_error = True
            elif type(value).__name__ == 'int' and len(value) >= 11:
                self.add_error(f'The \'{param}\' field cannot exceed 11 characters', ValueError)
                has_error = True

        return not has_error

    def validate(self):
        length_validation = self._validate_length()
        if not length_validation:
            return False

        return True
