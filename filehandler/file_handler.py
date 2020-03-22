import re

class FileHandler:
    def create_file_and_header(self, document_name: str, columns: str):
        formatted_columns = [f'"{column}"' for column in columns.split(', ')]
        with open(f'{document_name}.ddb', 'w') as f:
            f.write(','.join(formatted_columns) + '\n')

    def add_record(self, document_name: str, values: str):
        formatted_values = [f'"{value}"' for value in values.split(', ')]
        with open(f'{document_name}.ddb', 'a+') as f:
            f.write(','.join(formatted_values) + '\n')

    def file_to_list(self, document_name: str, columns: str):
        file_list = []
        selected_columns = []
        with open(f'{document_name}.ddb', 'r') as f:
            file_list = [[item for item in re.findall('[^"\n]+', line) if item != ','] for line in f.readlines()]
        return file_list

    def select_columns(self, document_name: str, columns: str):
        file_list = self.file_to_list(document_name, columns)
        selected_columns = []
        selected_list = []
        if columns == '*':
            selected_list = file_list
        else:
            selected_columns = [file_list[0].index(column) for column in columns.split(', ')]
            selected_list = [[file_list[row][index] for index in selected_columns] for row in range(len(file_list))]
        return selected_list

  
if __name__ == "__main__":
    file = FileHandler()
    file.create_file_and_header('somedoc', 'name, surname, age')
    file.add_record('somedoc', 'Pa,,,co, Daniell, 11')
    file.add_record('somedoc', 'Ro   cky, Daniell, 4')
    file.add_record('somedoc', 'Koles, Daniell, 2')