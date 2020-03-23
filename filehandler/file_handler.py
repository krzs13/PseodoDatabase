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

    def file_to_list(self, document_name: str):
        file_list = []  # file loaded to list with lists (rows of file)
        with open(f'{document_name}.ddb', 'r') as f:
            file_list = [[item for item in re.findall('[^"\n]+', line) if item != ','] for line in f.readlines()]
        return file_list

    def select_columns(self, document_name: str, columns: str):
        file_list = self.file_to_list(document_name)
        selected_columns = []  # list of selected columns indexes
        selected_list = []
        if columns == '*':
            selected_list = file_list
        else:
            selected_columns = [file_list[0].index(column) for column in columns.split(', ')]
            selected_list = [[file_list[row][index] for index in selected_columns] for row in range(len(file_list))]
        return selected_list

    def count_items(self, document_name: str, columns: str):
        file_list = self.file_to_list(document_name)
        column_list = [file_list[row][file_list[0].index(columns)] for row in range(len(file_list))]
        items_counted = []  # [[item, count]]
        for index in range(len(column_list)):
            if index == 0:
                items_counted.append([column_list[0], 'count'])  # header
            else:
                if [column_list[index], str(column_list[1:].count(column_list[index]))] not in items_counted:
                    items_counted.append([column_list[index], str(column_list[1:].count(column_list[index]))])
        return items_counted

    def delete_row(self, document_name: str, columns: str, values: str):
        file_list = self.file_to_list(document_name)
        rows_index = [row for row in range(1, len(file_list)) if file_list[row][file_list[0].index(columns)] == values]
        file_list = [file_list[row] for row in range(len(file_list)) if row not in rows_index]  # list without deleted rows
        formatted_row = []
        with open(f'{document_name}.ddb', 'w') as f:
            for row in file_list:
                formatted_row = [f'"{item}"' for item in row]
                f.write(','.join(formatted_row) + '\n')


if __name__ == "__main__":
    file = FileHandler()
    file.create_file_and_header('somedoc', 'name, surname, age')
    file.add_record('somedoc', 'Pa,,,co, Daniell, 11')
    file.add_record('somedoc', 'Ro   cky, Daniell, 4')
    file.add_record('somedoc', 'Koles, Daniell, 2')
    file.add_record('somedoc', 'Koles, Daniell, 2')
    # file.count_items('somedoc', 'name')
    # file.delete_row('somedoc', 'name', 'Koles')