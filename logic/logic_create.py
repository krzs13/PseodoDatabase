from filehandler.file_handler import FileHandler
from logic.logic_default import DefaultLogic

class CreateLogic(DefaultLogic):
    def __init__(self, document_name: str, columns: str, values: str):
        self.document_name = document_name
        self.columns = columns
        self.file_operation()

    def file_operation(self):
        self.file_handler = FileHandler()
        self.file_handler.create_file_and_header(self.document_name, self.columns)
