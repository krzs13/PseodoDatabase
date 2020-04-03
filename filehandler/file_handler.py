import os
import pickle
import re
from typing import List
import zipfile
<<<<<<< HEAD
from typing import List
=======
import exceptions.errors as errors
>>>>>>> changes


class FileHandler:
    def __init__(self, directory='database/', extension='.ddb'):
<<<<<<< HEAD
        self.extension = extension if extension.startswith('.') else '.' + extension
        self.directory = directory if directory.endswith('/') else directory + '/'
        self.__prepare_working_directory()

    def __prepare_working_directory(self):
        if not os.path.exists(f'{self.directory}'):
            os.mkdir(self.directory)

    def __full_path(self, document_name):
        return f'{self.directory}{document_name}{self.extension}'

    def create_file_and_header(self, document_name: str, columns: List[str]):
        formatted_columns = [f'"{column}"' for column in columns]
        with open(self.__full_path(document_name), 'w') as f:
            f.write(','.join(formatted_columns) + '\n')

    def add_record(self, document_name: str, values: List[str]):
        formatted_values = [f'"{value}"' for value in values]
        with open(self.__full_path(document_name), 'a+') as f:
            f.write(','.join(formatted_values) + '\n')
=======
        self.directory = directory if directory.endswith('/') else f'{directory}/'
        self.extension = extension if extension.startswith('.') else f'.{extension}'
        self.__prepare_working_directory()

    def __prepare_working_directory(self):
        if not os.path.exists(self.directory):
            os.mkdir(self.directory)

    def __full_path(self, document_name: str):
        return f'{self.directory}{document_name}{self.extension}'
>>>>>>> changes

    def __file_to_list(self, document_name: str):
        file_list = []  # file loaded to list with lists (rows of file)
        with open(self.__full_path(document_name), 'r') as f:
            file_list = [[item for item in re.findall('[^"\n]+', line) if item != ','] for line in f.readlines()]
        return file_list

<<<<<<< HEAD
    def select_columns(self, document_name: str, columns: List[str]):
        file_list = self.__file_to_list(document_name)

        if columns[0] == '*':
            return file_list

        selected_columns = [file_list[0].index(column) for column in columns]
        return [[row[index] for index in selected_columns] for row in file_list]

    def count_items(self, document_name: str, columns: List[str]):
        file_list = self.__file_to_list(document_name)
        column_list = [file_list[row][file_list[0].index(columns)] for row in range(len(file_list))]
        items_counted = []  # [[item, count]]
        for index in range(len(column_list)):
            if index == 0:
                items_counted.append([column_list[0], 'count'])  # header
            else:
                if [column_list[index], str(column_list[1:].count(column_list[index]))] not in items_counted:
                    items_counted.append([column_list[index], str(column_list[1:].count(column_list[index]))])
        return items_counted

    def delete_row(self, document_name: str, columns: List[str], values: List[str]):
        file_list = self.__file_to_list(document_name)
        rows_index = [row for row in range(1, len(file_list)) if file_list[row][file_list[0].index(columns)] == values]
        file_list = [file_list[row] for row in range(len(file_list)) if
                     row not in rows_index]  # list without deleted rows
        formatted_row = []
        with open(f'{document_name}.ddb', 'w') as f:
            for row in file_list:
                formatted_row = [f'"{item}"' for item in row]
                f.write(','.join(formatted_row) + '\n')

    def json_converter(self, document_name: str):
        file_list = self.__file_to_list(document_name)
        json_list = [{file_list[0][item]: file_list[row][item] for item in range(len(file_list[0]))} for row in
                     range(1, len(file_list))]
        return json_list
=======
    def create_file_and_header(self, document_name: str, columns: List[str]):
        formatted_columns = [f'"{column}"' for column in columns]
        with open(self.__full_path(document_name), 'w') as f:
            f.write(','.join(formatted_columns) + '\n')

    def add_record(self, document_name: str, values: List[str]):
        try:
            formatted_values = [f'"{value}"' for value in values]
            with open(self.__full_path(document_name), 'r') as f:
                columns = [item for item in re.findall('[^"\n]+', f.readline()) if item != ',']
                if len(columns) != len(values):
                    raise errors.WrongValuesQuantity(len(columns), len(values))
            with open(self.__full_path(document_name), 'a+') as f:
                f.write(','.join(formatted_values) + '\n')
        except FileNotFoundError:
            raise errors.FileNotFound(document_name)

    def select_columns(self, document_name: str, columns: List[str]):
        try:
            file_list = self.__file_to_list(document_name)
            if columns[0] == '*':
                return file_list
            selected_columns = [file_list[0].index(column) for column in columns]
            return [[row[index] for index in selected_columns] for row in file_list]
        except FileNotFoundError:
            raise errors.FileNotFound(document_name)
        except ValueError:
            raise errors.ColoumnNotFound(columns)

    def count_items(self, document_name: str, columns: List[str]):
        try:
            file_list = self.__file_to_list(document_name)
            column_list = [row[file_list[0].index(columns[0])] for row in file_list]
            items_counted = []  # [[item, count]]
            for index in range(len(column_list)):
                if index == 0:
                    items_counted.append([column_list[0], 'count'])  # header
                else:
                    if [column_list[index], str(column_list[1:].count(column_list[index]))] not in items_counted:
                        items_counted.append([column_list[index], str(column_list[1:].count(column_list[index]))])
            return items_counted
        except FileNotFoundError:
            raise errors.FileNotFound(document_name)
        except ValueError:
            raise errors.ColoumnNotFound(columns)
        
    def delete_row(self, document_name: str, columns: List[str], values: List[str]):
        try:
            file_list = self.__file_to_list(document_name)
            rows_index = [row for row in range(1, len(file_list)) if file_list[row][file_list[0].index(columns[0])] == values[0]]
            file_list = [file_list[row] for row in range(len(file_list)) if row not in rows_index]  # list without deleted rows
            formatted_row = []
            with open(self.__full_path(document_name), 'w') as f:
                for row in file_list:
                    formatted_row = [f'"{item}"' for item in row]
                    f.write(','.join(formatted_row) + '\n')
        except FileNotFoundError:
            raise errors.FileNotFound(document_name)
        except ValueError:
            raise errors.ColoumnNotFound(columns)

    def json_converter(self, document_name: str):
        try:
            file_list = self.__file_to_list(document_name)
            json_list = [{file_list[0][item]: file_list[row][item] for item in range(len(file_list[0]))} for row in range(1, len(file_list))]
            return json_list
        except FileNotFoundError:
            raise errors.FileNotFound(document_name)    
>>>>>>> changes

    def binary_converter(self, action: str, document_name: List[str]):
        names = document_name

        def save(documents: List[str]):
            for document in documents:
                if not os.path.exists(self.__full_path(document)):
                    raise errors.FileNotFound(document)
            package_name = input('Enter zip package name: ')
            package_path = f'{self.directory}{package_name}.zip'
            while os.path.exists(package_path):
                overwrite = input(f'{package_name}.zip already exists. Do you want to overwrite it? [Y/N]: ')
                if overwrite.lower() == 'y':
                    break
                else:
                    package_name = input('Enter new zip package name: ')
            with zipfile.ZipFile(package_path, 'w') as myzip:
                for document in documents:
                    bin_path = f'{self.directory}{document}.bin'
                    with open(self.__full_path(document), 'r') as f:
                        with open(bin_path, 'wb') as b:
                            pickle.dump(f.read(), b)
                    myzip.write(bin_path)
                    os.remove(bin_path)
            return [['Zip package directory:'], [package_path]]

        def load(packages: List[str]):
            for package in packages:
                package_path = f'{self.directory}{package}.zip'
                if not os.path.exists(package_path):
                    raise errors.FileNotFound(package)
                with zipfile.ZipFile(package_path, 'r') as myzip:
                    myzip.extractall()
<<<<<<< HEAD
                    documents = myzip.namelist()
                    for document in documents:
                        document_name = re.match('\w+', f'{document}').group()
                        while os.path.exists(f'{document_name}.ddb'):
                            overwrite = input(
                                f'{document_name}.ddb already exists. Do you want to overwrite it? [Y/N]: ')
=======
                    for document in myzip.namelist():
                        document_name = re.findall('\w+', f'{document}')[1]
                        while os.path.exists(self.__full_path(document_name)):
                            overwrite = input(f'{document_name}.ddb already exists. Do you want to overwrite it? [Y/N]: ')
>>>>>>> changes
                            if overwrite.lower() == 'y':
                                break
                            else:
                                document_name = input('Enter new document name: ')
                        with open(document, 'rb') as b:
                            with open(self.__full_path(document_name), 'w') as f:
                                f.write(pickle.load(b))
<<<<<<< HEAD
                        os.remove(f'{document}')

        if action == 'save':
            return save(names)
        elif action == 'load':
            return load(names)


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
=======
                        os.remove(document)
        
        if action == 'save':
            return save(names)
        elif action == 'load':
            return load(names)
>>>>>>> changes
