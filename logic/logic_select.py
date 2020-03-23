from logic.logic_default import DefaultLogic
from userinterface.user_interface import UserInterface

class SelectLogic(DefaultLogic):
    def __init__(self, document_name, columns, values):
        super(SelectLogic, self).__init__(document_name, columns, values)
        self.selected_list = self.file_operation()
        self.ui = UserInterface()
        self.ui.user_output(self.selected_list)

    def file_operation(self):
        return self.file_handler.select_columns(self.document_name, self.columns)