import exceptions.errors as errors
from logic.command_interpreter import CommandInterpreter
from logic.logic_add import AddLogic
from logic.logic_create import CreateLogic
from logic.logic_count import CountLogic
from logic.logic_delete import DeleteLogic
from logic.logic_export import ExportLogic
from logic.logic_import import ImportLogic
from logic.logic_json import JsonLogic
from logic.logic_select import SelectLogic
from userinterface.user_interface import UserInterface


class FrontController:
    def __init__(self):
        self.ui = UserInterface()
        self.ci = CommandInterpreter()
        self.logic_dictionary = {
<<<<<<< HEAD
            'create': CreateLogic,
            'add': AddLogic,
            'select': SelectLogic,
            'count': CountLogic,
            'delete': DeleteLogic,
            'json': JsonLogic,
            'export': ExportLogic,
            'import': ImportLogic
        }
=======
            'create': CreateLogic, 
            'add': AddLogic, 
            'select': SelectLogic, 
            'count': CountLogic, 
            'delete': DeleteLogic, 
            'json': JsonLogic,
            'export': ExportLogic, 
            'import': ImportLogic
            }
>>>>>>> changes
        self.ui.say_hello()

    def run(self):
        while True:
            try:
                command = self.ui.user_input()
                command_dictionary = self.ci.interpreter(command)
<<<<<<< HEAD
                # w tym miejscu nie musi byc get. W przypadku podstaiwienia nona za klucz do "logic_dictionary" i tak
                # dostaniemy KeyError. Błąd należy obsłużyć
                self.logic_dictionary[command_dictionary['command_name']](command_dictionary.get('document_name'),
                                                                          command_dictionary.get('columns'),
                                                                          command_dictionary.get('values'))
            except Exception as e:  # to mogłoby nawet zostać, jako ostatnia linia obrony. Powinieneś jednak lepiej
                # zaimplementować obsługę wyjątków. Dodałem ją teraz tylko dla wygody.
                print("Unexpected error:")
                print(e)
=======
                self.logic_dictionary[command_dictionary['command_name']](command_dictionary.get('document_name'), 
                command_dictionary.get('columns'), command_dictionary.get('values'))
            except KeyError:
                print(f'{command_dictionary["command_name"]} does not exist.')
            except TypeError:
                print('Command is not valid.')
            except (errors.ColoumnNotFound, errors.FileNotFound, errors.WrongValuesQuantity) as error:
                print(error)
>>>>>>> changes
