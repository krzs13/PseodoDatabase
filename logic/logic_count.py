from logic.logic_default import DefaultLogic
from userinterface.user_interface import UserInterface


class CountLogic(DefaultLogic):
    def __init__(self, document_name, columns, values):
        super().__init__(document_name, columns, values)
        self.items_counted = self.file_operation()
        self.ui = UserInterface()
        self.ui.user_output(self.items_counted)

    def file_operation(self):
        return self.file_handler.count_items(self.document_name, self.columns)

