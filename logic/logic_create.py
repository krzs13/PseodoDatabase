from logic.logic_default import DefaultLogic

class CreateLogic(DefaultLogic):
    def __init__(self, document_name, columns, values):
        super(CreateLogic, self).__init__(document_name, columns, values)
        self.file_operation()

    def file_operation(self):
        self.file_handler.create_file_and_header(self.document_name, self.columns)
