'''
# This is a class for processing CSV files, including readring and writing CSV data, as well as processing specific operations and saving as a new CSV file.

import csv

class CSVProcessor:

    def __init__(self):
        pass

    def read_csv(self, file_name):
        """
        Read the csv file by file_name, get the title and data from it
        :return title, data: (list, list), first row is title, the rest is data
        """

    def write_csv(self, data, file_name):
        """
        Write data into a csv file.
        :return:int, if success return 1, or 0 otherwise
        """

    def process_csv_data(self, N, save_file_name):
        """
        Read a csv file into variable title and data.
        Only remain the N th (from 0) column data and Capitalize them, store the title and new data into a new csv file.
        Add '_process' suffix after old file name, as a new file name.
        :return:int, if success return 1, or 0 otherwise
        """
'''

import csv


class CSVProcessor:

    def __init__(self):
        pass

    def read_csv(self, file_name):
        data = []
        with open(file_name, 'r') as file:
            reader = csv.reader(file)
            title = next(reader)
            for row in reader:
                data.append(row)
        return title, data

    def write_csv(self, data, file_name):
        try:
            with open(file_name, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(data)
            return 1
        except:
            return 0

    def process_csv_data(self, N, save_file_name):
        title, data = self.read_csv(save_file_name)
        column_data = [row[N] for row in data]
        column_data = [row.upper() for row in column_data]
        new_data = [title, column_data]
        return self.write_csv(new_data, save_file_name.split('.')[0] + '_process.csv')
