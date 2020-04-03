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
            'create': CreateLogic, 
            'add': AddLogic, 
            'select': SelectLogic, 
            'count': CountLogic, 
            'delete': DeleteLogic, 
            'json': JsonLogic,
            'export': ExportLogic, 
            'import': ImportLogic
            }
        self.ui.say_hello()

    def run(self):
        while True:
            try:
                command = self.ui.user_input()
                command_dictionary = self.ci.interpreter(command)
                self.logic_dictionary[command_dictionary['command_name']](command_dictionary.get('document_name'), 
                command_dictionary.get('columns'), command_dictionary.get('values'))
            except KeyError:
                print(f'{command_dictionary["command_name"]} does not exist.')
            except TypeError:
                print('Command is not valid.')
            except (errors.ColoumnNotFound, errors.FileNotFound, errors.WrongValuesQuantity) as error:
                print(error)