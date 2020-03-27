from logic.logic_default import DefaultLogic
from userinterface.user_interface import UserInterface

class ImportLogic(DefaultLogic):
    def __init__(self, document_name, columns, values):
        super(ImportLogic, self).__init__(document_name, columns, values)
        self.package_directory = self.file_operation()
        self.ui = UserInterface()
        self.ui.user_output(self.package_directory)


    def file_operation(self):
        return self.file_handler.binary_converter('save', self.document_name)