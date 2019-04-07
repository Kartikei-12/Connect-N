'''
@author: Kartikei Mittal
@email: kartikeimittal@gmail.com
connect_n.py file
Contains main module of this repositry.
https://github.com/Kartikei-12/Connect-N
'''

__author__ = 'Kartikei Mittal'
__email__ = 'kartikeimittal@gmail.com'

import os
import numpy

FILE_PATH = os.path.dirname(os.path.realpath(__file__)) + '/version.txt'


class ConnectNGame:
    '''
    Main module class used Connect-N game.
    https://github.com/Kartikei-12/Connect-N
    '''
    
    __version__ = '0.1d.'

    def __init__(self, num_rows = 6, num_columns = 7, n = 4):
        '''
        Instantiate function for class ConnectNGame
        '''
        
        if not isinstance(num_rows, int):
            raise ValueError(
                "Error: num_rows except <class 'int'> not {}"\
                    .format(type(num_rows)))
        if not isinstance(num_columns, int):
            raise ValueError(
                "Error: num_columns except <class 'int'> not {}"\
                    .format(type(num_columns)))
        if not isinstance(n, int):
            raise ValueError(
                "Error: n except <class 'int'> not {}"\
                .format(type(n)))
        
        try: # Integrating file number.
            self.__version__ += open(FILE_PATH, 'r').read()
        except FileNotFoundError: pass

        self.NUM_ROWS = num_rows
        self.NUM_COLUMNS = num_columns
        self.N = n

    def __repr__(self):
        '''
        Representation format:
            <class 'CLASS NAME', NUMBER_OF_ROWS NUMBER_OF_COLUMNS CONNECT_LENGTH>
        '''
        return "<class '{0}', {1} {2} {3} >"\
            .format(
                self.__class__.__name__,
                self.NUM_ROWS,
                self.NUM_COLUMNS,
                self.N
            )
