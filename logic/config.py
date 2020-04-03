class Config:
    def __init__(self):
        self.valid_regex = {
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
        self.split_fields = ['columns', 'values']