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