from abc import ABC, abstractmethod

class DefaultLogic(ABC):
    @abstractmethod
    def file_operation(self, document_name, columns, values):
        pass