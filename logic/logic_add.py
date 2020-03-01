from filehandler.file_handler import FileHandler
from logic.logic_default import DefaultLogic

class AddLogic(DefaultLogic):
    def __init__(self, document_name: str, columns: str, values: str):
        self.document_name = document_name
        self.values = values
        self.file_operation()

    def file_operation(self):
        self.file_handler = FileHandler()
        self.file_handler.add_record(self.document_name, self.values)