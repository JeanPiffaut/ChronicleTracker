from common.domain.module_model import ModuleModel


class TestModuleModel:

    def test_add_error(self):
        module_model = ModuleModel()
        module_model.add_error("Error 1")
        module_model.add_error("Error 2")
        assert module_model.get_errors() == [{'msj': "Error 1", 'type_error': Exception},
                                             {'msj': "Error 2", 'type_error': Exception}]

    def test_set_errors(self):
        module_model = ModuleModel()
        module_model.set_errors(
            [{'msj': "Error 3", 'type_error': ValueError}, {'msj': "Error 4", 'type_error': ValueError}])
        assert module_model.get_errors() == [{'msj': "Error 3", 'type_error': ValueError},
                                             {'msj': "Error 4", 'type_error': ValueError}]
