import os
import pickle
import re
import zipfile

class FileHandler:
    def __init__(self, directory='database'):
        self.directory = directory
        self.set_working_directory()

    def set_working_directory(self):
        if not os.path.exists(f'{self.directory}'):
            os.mkdir(self.directory)
        os.chdir(self.directory)

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

    def json_converter(self, document_name: str):
        file_list = self.file_to_list(document_name)
        json_list = [{file_list[0][item]: file_list[row][item] for item in range(len(file_list[0]))} for row in range(1, len(file_list))]
        return json_list

    def binary_converter(self, action: str, document_name: str):
        names = document_name.split(', ')
        if action == 'save':
            return save(names)
        elif action == 'load':
            return load(names)

        def save(documents: list):
            package_name = input('Enter zip package name: ')
            package_directory = [['Zip package directory:']]
            package_directory.append([f'{self.directory}/{package_name}.zip'])
            overwrite = ''
            while os.path.exists(f'{package_name}.zip'):
                overwrite = input(f'The {package_name}.zip already exists. Do you want to overwrite it? [Y/N]: ')
                if overwrite.lower() == 'y':
                    break
                else:
                    package_name = input('Enter new zip package name: ')
            with zipfile.ZipFile(f'{package_name}.zip', 'w') as myzip:
                for document in documents:
                    with open(f'{document}.ddb', 'r') as f:
                        with open(f'{document}.bin', 'wb') as b:
                            pickle.dump(f.read(), b)
                    myzip.write(f'{document}.bin')
                    os.remove(f'{document}.bin')
            return package_directory

        def load(packages: list):
            documents = []
            document_name = ''
            package_name = ''
            overwrite = ''
            for package in packages:
                package_name = package.split('/')[-1]  # last item in list is last element in path
                with zipfile.ZipFile(f'{package_name}', 'r') as myzip:
                    myzip.extractall()
                    documents = myzip.namelist()
                    for document in documents:
                        document_name = re.match('\w+', f'{document}').group()
                        while os.path.exists(f'{document_name}.ddb'):
                            overwrite = input(f'{document_name}.ddb already exists. Do you want to overwrite it? [Y/N]: ')
                            if overwrite.lower() == 'y':
                                break
                            else:
                                document_name = input('Enter new document name: ')
                        with open(f'{document}', 'rb') as b:
                            with open(f'{document_name}.ddb', 'w') as f:
                                f.write(pickle.load(b))
                        os.remove(f'{document}')


if __name__ == "__main__":
    file = FileHandler()
    file.create_file_and_header('somedoc', 'name, surname, age')
    file.add_record('somedoc', 'Pa,,,co, Daniell, 11')
    file.add_record('somedoc', 'Ro   cky, Daniell, 4')
    file.add_record('somedoc', 'Koles, Daniell, 2')
    file.add_record('somedoc', 'Koles, Daniell, 2')
    # file.binary_converter('save', 'somedoc')
    # file.binary_converter('load', 'somepac')
    # file.json_converter('somedoc')
    # file.count_items('somedoc', 'name')
    # file.delete_row('somedoc', 'name', 'Koles')