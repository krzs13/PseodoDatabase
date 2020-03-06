class FileHandler:
    def create_file_and_header(self, document_name: str, columns: str):
        with open(f'{document_name}.ddb', 'w') as f:
            f.write(''.join(columns.split()) + '\n')

    def add_record(self, document_name: str, values: str):
        formatted_values = [f'"{value}"' for value in values.split(', ')]
        with open(f'{document_name}.ddb', 'a+') as f:
            f.write(','.join(formatted_values) + '\n')

    def select_columns(self, document_name: str, columns: str):
        selected_columns = [column for column in columns.split(', ')]
        file_list = []
        rows_list = []
        with open(f'{document_name}.ddb', 'r') as f:
            file_list = list(map(lambda element: element[0:-1] if element[-1:] == '\n' else element, f.readlines()))
            file_list = [element.split(',') for element in file_list]
            for x in range(len(file_list)):
                for y in range(len(file_list[x])):
                    file_list[x][y] = file_list[x][y][1:-1] if file_list[x][y][0] == '"' and file_list[x][y][-1] else file_list[x][y]
            
            rows_list = [[] for row in range(len(file_list))]
            for column in selected_columns:
                rows_list[0].append(column)
                column_index = file_list[0].index(column)
                for row in range(1, len(file_list)):
                    rows_list[row].append(file_list[row][column_index])

            for element in rows_list[0]:
                print(f'{element + ((15 - len(element)) * " ")}', end='')
            print()
            for element in rows_list[0]:
                print(f'{15 * "-"}', end='')
            print()
            for row in rows_list[1:]:
                for element in row:
                    print(f'{element + ((15 - len(element)) * " ")}', end='')
                print()
                

if __name__ == "__main__":
    file = FileHandler()
    file.create_file_and_header('somedoc', 'name, surname, age')
    file.add_record('somedoc', 'Paco, Daniell, 11')
    file.add_record('somedoc', 'Rocky, Daniell, 4')
    file.add_record('somedoc', 'Koles, Daniell, 2')
    file.select_columns('somedoc', 'name, age, surname')