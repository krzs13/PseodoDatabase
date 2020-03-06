from logic.logic_default import DefaultLogic

class SelectLogic(DefaultLogic):
    def __init__(self, document_name, columns, values):
        super(SelectLogic, self).__init__(document_name, columns, values)

    def file_operation(self):
        self.file_handler.select_columns(self.document_name, self.columns)