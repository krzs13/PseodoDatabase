class FileHandler:
    def create_file_and_header(self, document_name: str, columns: str):
        with open(f'{document_name}.csv', 'w') as f:
            f.write(''.join(columns.split()) + '\n')

    def add_record(self, document_name: str, values: str):
        formatted_values = []
        with open(f'{document_name}.csv', 'a+') as f:
            for value in values.split(', '):
                formatted_values.append(f'"{value}"')
            print(formatted_values)
            f.write(','.join(formatted_values) + '\n')


if __name__ == "__main__":
    file = FileHandler()
    file.create_file_and_header('somedoc', 'aaa, bbb, ccc')
    file.add_record('somedoc', 'ddd, eee, fff')
    file.add_record('somedoc', 'dd   d,        e   ee, f   ff')