from typing import List


class Error(Exception):
    pass

class ColoumnNotFound(Error):
    def __init__(self, columns: List[str]):
        self.variation = ['', 'es'] if len(columns) == 1 else ['s', '']
        self.message = f'Column{self.variation[0]} {", ".join(columns)} do{self.variation[1]} not exist.'
        super().__init__(self.message)

class FileNotFound(Error):
    def __init__(self, document_name: str):
        self.message = f'{document_name} is not found.'
        super().__init__(self.message)

class WrongValuesQuantity(Error):
    def __init__(self, columns_quantity: int, values_quantity: int):
        self.variation = 'little' if columns_quantity > values_quantity else 'many'
        self.message = f'Too {self.variation} values: {values_quantity} given but {columns_quantity} needed.'
        super().__init__(self.message)