import re

class CommandInterpreter:
    def __init__(self):
        self.VALID_REGEX = {
            'create': {
                'regex' : '\s*CREATE\s+DOCUMENT\s+(\w*)\s+\((.*)\)',
                'order' : ['document_name', 'columns']
                },
            'add': {
                'regex' : '\s*ADD\s+\((.*)\)\s+TO\s+(\w*)',
                'order' : ['values', 'document_name']
                },
            'select': {
                'regex' : '\s*SELECT\s+\((.*)\)\s+FROM\s+(\w*)',
                'order' : ['columns', 'document_name']
                },
            'count': {
                'regex' : '\s*COUNT\s+DISTINCT\s+\((.*)\)\s+FROM\s+(\w*)',
                'order' : ['columns', 'document_name']
                },
            'delete': {
                'regex' : '\s*DELETE\s+FROM\s+(\w*)\s+WHERE\s+(.*)\s*=\s*(.*)',
                'order' : ['document_name', 'columns', 'values']
                },
            'json': {
                'regex' : '\s*JSON\s+(\w*)',
                'order' : ['document_name']
                },
            'import': {
                'regex' : '\s*IMPORT\s+(.*)',
                'order' : ['document_name']
            }
        }
    
    def interpreter(self, command: str):
        selected_command = None
        for command_name, valid_regex in self.VALID_REGEX.items():
            selected_command = re.findall(valid_regex['regex'], command, re.I)
            if len(selected_command):
                selected_command = selected_command[0]
                if command_name == 'delete':
                    return dict({
                        'command_name': command_name,
                        valid_regex['order'][0]: selected_command[0],
                        valid_regex['order'][1]: selected_command[1],
                        valid_regex['order'][2]: selected_command[2]
                    })
                elif command_name in ['json', 'import']:
                    return dict({
                        'command_name': command_name,
                        valid_regex['order'][0]: selected_command
                    })
                else:
                    return dict({
                        'command_name': command_name,
                        valid_regex['order'][0]: selected_command[0],
                        valid_regex['order'][1]: selected_command[1]
                    })