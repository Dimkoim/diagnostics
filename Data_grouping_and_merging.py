#Data preprocessing 
from os import listdir
from os.path import isfile, join
from itertools import groupby
import pandas as pd 
import os 
import numpy as np


class files_to_df(object):
    
    '''
    A class that groups that gets as ipput a folder containing txt files, it groups the files based on a criterion, merge them and returns
    the dataframes of the each different category
    
   :param directory: the folder that contains the txt files
   :return: a dictionary containing the dataframes
        '''
    def __init__(self, directory):
        self.directory = directory
        self.onlyfiles = [f for f in listdir(directory) if isfile(join(directory, f))]
        self.all_channels = self.grouping(self.onlyfiles)  
        self.keys = list(self.all_channels.keys())               
    
    def grouping(self, files):
        '''
        A class method that defines the different categories of data
        '''
        all_channels = []
        for file in files:
            string = [elem for i,elem in enumerate(file) if elem.isdigit()]
            all_channels.append(int(string[0]))
        all_channels = set(all_channels)
        dictionary = {key: [] for key in all_channels}
        return dictionary  
                      
    
    def df(self):
        '''
        A class method that calculates the dataframes
        '''
        for key in self.keys:
            for file in self.onlyfiles:
                string = [''.join(g) for _, g in groupby(file, str.isalpha)]
                if  int(string[1][0])==key:
                    self.all_channels[key].append(file)
        
        df = dict.fromkeys(self.keys)
        for key in self.keys:
            resistances = ['resistance {}'.format(i) for i in np.arange(int(key))]
            df_names=['Date','time','minimum', 'maximum', 'wire resistance'] + resistances 
            appended_data = []
            for file in self.all_channels[key]:
                path =  os.path.join(self.directory, file)
                print (path)
                array = pd.read_csv(path, 
                                    encoding='cp1252',
                                    header = None, 
                                    sep = ';', 
                                    usecols = np.arange((len(df_names))),
                                    names= df_names,
                                    parse_dates=[[0,1]]
                                    )

                appended_data.append(array)
            appended_data = pd.concat(appended_data, axis=0)
            df[key] = appended_data
        return df
