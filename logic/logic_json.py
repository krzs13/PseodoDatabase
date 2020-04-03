from logic.logic_default import DefaultLogic
from userinterface.user_interface import UserInterface


class JsonLogic(DefaultLogic):
    def __init__(self, document_name, columns, values):
        super().__init__(document_name, columns, values)
        self.json_list = self.file_operation()
        self.ui = UserInterface()
        self.ui.json_output(self.json_list)

    def file_operation(self):
        return self.file_handler.json_converter(self.document_name)
