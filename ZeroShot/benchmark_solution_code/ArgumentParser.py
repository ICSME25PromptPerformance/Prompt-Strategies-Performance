'''
# This is a class for parsing command line arguments to a dictionary.

class ArgumentParser:
    def __init__(self):
        """
        Initialize the fields.
        """

    def parse_arguments(self, command_string):
        """
        Parses the given command line argument string and invoke _convert_type to stores the parsed result in specific type in the arguments dictionary.
        Checks for missing required arguments, if any, and returns False with the missing argument names, otherwise returns True.
        :return tuple: (True, None) if parsing is successful, (False, missing_args) if parsing fails,
            where missing_args is a set of the missing argument names which are str.
        """

    def get_argument(self, key):
        """
        Retrieves the value of the specified argument from the arguments dictionary and returns it.
        :return: The value of the argument, or None if the argument does not exist.
        """

    def add_argument(self, arg, required=False, arg_type=str):
        """
        Adds an argument to self.types and self.required.
        Check if it is a required argument and store the argument type.
        If the argument is set as required, it wull be added to the required set.
        The argument type and name are stored in the types dictionary as key-value pairs.
        """

    def _convert_type(self, arg, value):
        """
        Try to convert the type of input value by searching in self.types.
        :return: return corresponding value in self.types if convert successfully, or the input value oherwise
        """
'''



class ArgumentParser:
    def __init__(self):
        self.arguments = {}
        self.required = set()
        self.types = {}

    def parse_arguments(self, command_string):
        args = command_string.split()[1:]
        for i in range(len(args)):
            arg = args[i]
            if arg.startswith('--'):
                key_value = arg[2:].split('=')
                if len(key_value) == 2:
                    self.arguments[key_value[0]] = self._convert_type(key_value[0], key_value[1])
                else:
                    self.arguments[key_value[0]] = True
            elif arg.startswith('-'):
                key = arg[1:]
                if i + 1 < len(args) and not args[i + 1].startswith('-'):
                    self.arguments[key] = self._convert_type(key, args[i + 1])
                else:
                    self.arguments[key] = True
        missing_args = self.required - set(self.arguments.keys())
        if missing_args:
            return False, missing_args

        return True, None

    def get_argument(self, key):
        return self.arguments.get(key)

    def add_argument(self, arg, required=False, arg_type=str):
        if required:
            self.required.add(arg)
        self.types[arg] = arg_type

    def _convert_type(self, arg, value):
        try:
            return self.types[arg](value)
        except (ValueError, KeyError):
            return value

