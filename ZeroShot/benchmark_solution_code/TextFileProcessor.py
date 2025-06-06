'''
# The class handles reading, writing, and processing text files. It can read the file as JSON, read the raw text, write content to the file, and process the file by removing non-alphabetic characters.

import json

class TextFileProcessor:
    def __init__(self, file_path):
        """
        Initialize the file path.
        """

    def read_file_as_json(self):
        """
        Read the self.file_path file as json format.
        if the file content doesn't obey json format, the code will raise error.
        :return data: dict if the file is stored as json format, or str/int/float.. according to the file content otherwise.
        """

    def read_file(self):
        """
        Read the return the content of self.file_path file.
        :return: the same return as the read() method
        """

    def write_file(self, content):
        """
        Write content into the self.file_path file, and overwrite if the file has already existed.
        :param content: any content
        """

    def process_file(self):
        """
        Read the self.file_path file and filter out non-alphabetic characters from the content string.
        Overwrite the after-processed data into the same self.file_path file.
        """
'''

import json


class TextFileProcessor:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_file_as_json(self):
        with open(self.file_path, 'r') as file:
            data = json.load(file)

        return data

    def read_file(self):
        with open(self.file_path, 'r') as file:
            return file.read()

    def write_file(self, content):
        with open(self.file_path, 'w') as file:
            file.write(content)

    def process_file(self):
        content = self.read_file()
        content = ''.join([char for char in content if char.isalpha()])
        self.write_file(content)
        return content
