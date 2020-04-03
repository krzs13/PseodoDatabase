from logic.logic_default import DefaultLogic
from userinterface.user_interface import UserInterface


class ImportLogic(DefaultLogic):
    def __init__(self, document_name, columns, values):
        super().__init__(document_name, columns, values)
        self.file_operation()

    def file_operation(self):
        self.file_handler.binary_converter('load', self.document_name)