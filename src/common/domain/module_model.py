import re


class ModuleModel:
    def __init__(self):
        self._errors = []

    def add_error(self, error_msj: str, type_error=Exception):
        self._errors.append({'msj': error_msj, 'type_error': type_error})

    def set_errors(self, errors=None):
        if errors is None:
            errors = list()
        self._errors = errors

    def delete_errors(self):
        self._errors = []

    def get_errors(self):
        return self._errors

    def _validate_length(self):
        has_error = False
        params = self.__dict__
        for param, value in params.items():
            if value is not None and type(value).__name__ == 'str' and len(value) >= 255:
                self.add_error(f'The \'{param}\' field cannot exceed 255 characters', ValueError)
                has_error = True
            elif value is not None and type(value).__name__ == 'int' and len(str(value)) >= 11:
                self.add_error(f'The \'{param}\' field cannot exceed 11 characters', ValueError)
                has_error = True

        return not has_error

    def validate(self):
        result = self._validate_length()
        return result

    def sanitize_for_mysql(self):
        params = self.__dict__
        for attr, value in params.items():
            if isinstance(value, str):
                params[attr] = re.sub(r'[^\w\s\-]', '', value.strip())
