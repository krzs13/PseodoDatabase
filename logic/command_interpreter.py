import re
from logic.config import Config


class CommandInterpreter:
    def __init__(self):
        self.config = Config()
            
    def __split_field(self, field: str, values: str):
        if field in self.config.split_fields:
            return [re.match('\S.*\S|\w|\s', value).group() for value in values.split(', ')]
        return values

    def interpreter(self, command: str):
        for command_name, valid_regex in self.config.valid_regex.items():
            selected_command = re.findall(valid_regex['regex'], command, re.I)
            if len(selected_command):
                selected_command = selected_command[0] if type(selected_command[0]) == tuple else tuple(selected_command)
                command_dictionary = {'command_name': command_name}
                command_dictionary.update({
                    key: self.__split_field(key, selected_command[index]) for index, key in enumerate(valid_regex['order'])
                })
                return command_dictionary
