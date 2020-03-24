class UserInterface:
    def say_hello(self):
        print('Hello')
        print('Version 0.0.1')

    def user_input(self):
        return input('>>> ')
    
    def user_output(self, file_list: list):
        for row in range(len(file_list)):
            if row == 0:
                for index in range(len(file_list[row])):
                    print(file_list[row][index], end=(15 - len(file_list[row][index])) * (' '))
                print('\n' + (15 * len(file_list[row]) * '-'))
            else:
                for index in range(len(file_list[row])):
                    print(file_list[row][index], end=(15 - len(file_list[row][index])) * (' '))
                print()
    
    def json_output(self, json_list: list):
        for row in range(len(json_list)):
            counter = 0
            print('{')
            for item in json_list[row].items():
                counter += 1
                if counter < len(json_list[row]):
                    print(f'    "{item[0]}": "{item[1]}",')
                else:
                    print(f'    "{item[0]}": "{item[1]}"') 
            if row < len(json_list) - 1:
                print('},')
            else:
                print('}')