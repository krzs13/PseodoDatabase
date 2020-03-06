from abc import ABC, abstractmethod
from filehandler.file_handler import FileHandler

class DefaultLogic(ABC):
    def __init__(self, document_name: str, columns: str, values: str):
        self.document_name = document_name
        self.columns = columns
        self.values = values
        self.file_handler = FileHandler()
        self.file_operation()

    @abstractmethod
    def file_operation(self):
        pass