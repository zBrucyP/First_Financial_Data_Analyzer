import os
import pandas as pd


class FF_File:

    # CLASS VARIABLES
    file_path = ''
    file_name = ''
    df_file_data = {}

    # CLASS CONSTANTS
    col = [  # column structure for First Financial data extracts
        'Acc Num',
        'Post Date',
        'Check',
        'Description',
        'Debit',
        'Credit',
        'Status',
        'Balance'
    ]
    ACC_NUM = 0
    POST_DATE = 1
    CHECK = 2
    DESCRIPTION = 3
    DEBIT = 4
    CREDIT = 5
    STATUS = 6
    BALANCE = 7


    def __init__(self, path):
        # get path to file
        self.file_path = path

        # extract name of file from path
        self.file_name = str(os.path.basename(path))

        # ensure path and file structure is acceptable
        self.validate_file()

        # extract data
        self.extract_data()

        print(self.df_file_data)


    def get_file_name(self):
        '''
        getter for name of file object from path
        :return: str of file name
        '''
        return self.file_name

    def validate_file(self):
        1+1

    def extract_data(self):
        '''
        extracts data from file path of object into Pandas DataFrame
        :return: N/A
        '''
        self.df_file_data = pd.read_csv(self.file_path, names=self.col, header=0)

    def get_file_contents(self):
        '''
        getter for file contents as a Pandas DataFrame
        :return: DataFrame
        '''
        return self.df_file_data

