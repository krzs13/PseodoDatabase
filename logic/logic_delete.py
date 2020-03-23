from logic.logic_default import DefaultLogic

class DeleteLogic(DefaultLogic):
    def __init__(self, document_name, columns, values):
        super(DeleteLogic, self).__init__(document_name, columns, values)
        self.file_operation()

    def file_operation(self):
        self.file_handler.delete_row(self.document_name, self.columns, self.values)