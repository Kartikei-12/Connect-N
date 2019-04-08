'''
@author: Kartikei Mittal
@email: kartikeimittal@gmail.com
connect_n.py file
Contains main module of this repositry.
https://github.com/Kartikei-12/Connect-N
'''

__author__ = 'Kartikei Mittal'

# Python module(s)
import os
import numpy as np

# User module(s)
from default_variables import *

FILE_PATH = os.path.dirname(os.path.realpath(__file__)) + '/version.txt'


class ConnectNGame:
    '''
    Main module class used Connect-N game.
    https://github.com/Kartikei-12/Connect-N
    '''
    
    __version__ = '0.1d.'

    def __init__(self, num_rows = ROWS, num_col = COLUMNS, n = N):
        '''
        Instantiate function for class ConnectNGame
        '''
        
        if not isinstance(num_rows, int):
            raise ValueError(
                "Error: num_rows except <class 'int'> not {}"\
                    .format(type(num_rows)))
        if not isinstance(num_col, int):
            raise ValueError(
                "Error: num_col except <class 'int'> not {}"\
                    .format(type(num_col)))
        if not isinstance(n, int):
            raise ValueError(
                "Error: n except <class 'int'> not {}"\
                .format(type(n)))
        
        try: # Integrating file number.
            with open(FILE_PATH, 'r') as f:
                self.__version__ += f.read()
                f.close()
        except FileNotFoundError: pass

        self.num_rows = num_rows
        self.num_col = num_col
        self.n = n
        self.board = np.zeros((self.num_rows, self.num_col))

    def print_board(self):
        # Helper function which prints the board
        print(np.flip(self.board, 0))

    def __repr__(self):
        '''
        Representation format:
            <class 'CLASS NAME', NUMBER_OF_ROWS NUMBER_OF_COLUMNS CONNECT_LENGTH>
        '''
        return "<class '{0}', {1} {2} {3} >"\
            .format(
                self.__class__.__name__,
                self.num_rows,
                self.num_col,
                self.n
            )
