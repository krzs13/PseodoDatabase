from userinterface.userinterface import UserInterface
from logic.commandinterpreter import CommandInterpreter
from logic.createlogic import CreateLogic


class FrontController:
    def __init__(self):
        self.ui = UserInterface()
        self.ci = CommandInterpreter()
        self.ui.say_hello()
        self.logic_dictionary = {'create': CreateLogic, 'add': AddLogic, 'select': SelectLogic}

    def run(self):
        while True:
            command = self.ui.user_input()
            command_dictionary = self.ci.interpreter(command)
            self.logic_dictionary[command_dictionary[0]](command_dictionary.get('document_name'), 
            command_dictionary.get('columns'), command_dictionary.get('values'))

