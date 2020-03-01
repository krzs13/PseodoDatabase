from filehandler.filehandler import FileHandler
from logic.defaultlogic import DefaultLogic

class CreateLogic(DefaultLogic):
    def file_operation(self, document_name, columns, value):
        self.document_name = document_name
        self.columns = columns
