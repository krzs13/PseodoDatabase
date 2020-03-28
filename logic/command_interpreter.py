import re


class CommandInterpreter:
    def __init__(self):
        # dobrze byłoby przenieść to do jakiegoś pliku conf.py
        self.VALID_REGEX = {
            'create': {
                'regex': '\s*CREATE\s+DOCUMENT\s+(\w*)\s+\((.*)\)',
                'order': ['document_name', 'columns']
            },
            'add': {
                'regex': '\s*ADD\s+\((.*)\)\s+TO\s+(\w*)',
                'order': ['values', 'document_name']
            },
            'select': {
                'regex': '\s*SELECT\s+\((.*)\)\s+FROM\s+(\w*)',
                'order': ['columns', 'document_name']
            },
            'count': {
                'regex': '\s*COUNT\s+DISTINCT\s+\((.*)\)\s+FROM\s+(\w*)',
                'order': ['columns', 'document_name']
            },
            'delete': {
                'regex': '\s*DELETE\s+FROM\s+(\w*)\s+WHERE\s+(.*)\s*=\s*(.*)',
                'order': ['document_name', 'columns', 'values']
            },
            'json': {
                'regex': '\s*JSON\s+(\w*)',
                'order': ['document_name']
            },
            'export': {
                'regex': '\s*EXPORT\s+(.*)',
                'order': ['document_name']
            },
            'import': {
                'regex': '\s*IMPORT\s+FROM\s+(.*)',
                'order': ['document_name']
            }
        }

        # to tez przenieść do conf.py
        self.split_fields = {
            'columns': ',',
            'values': ','
        }

    # interpreter powinien zwracać dane w całości zinterpretowane
    # dla kolumn czy wartości oznacza to zwrócenie listy, a nie stringa np podany string 'a, b     ,    c   '
    # musi zwrócić listę ['a', 'b', 'c']
    # w tym miejscu powinna odbywać się też implementacja zadania
    # "Tworzenie rekordu - dodawanie rekordu do dokumentu" - części z gwiazdką.
    def __split_field(self, field: str, value: str):
        if field in self.split_fields:
            return value.replace(' ', '').split(self.split_fields[field])  # to musi zostać zmienione dla zadania z *
        return value

    def interpreter(self, command: str):
        # definiowanie selected_command nie jest konieczne w tym miejscu - w każdej iteracji i tak nadajesz warość
        for command_name, valid_regex in self.VALID_REGEX.items():
            selected_command = re.findall(valid_regex['regex'], command, re.I)
            # wartość będzie przechowywana przez całą iteracje
            if len(selected_command):
                selected_command = selected_command[0]

                temp = {'command_name': command_name}
                temp.update({
                    key: self.__split_field(key, selected_command[i]) for i, key in enumerate(valid_regex['order'])}
                )

                return temp
