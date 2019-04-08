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
from .utility import getVersion
from default_variables import *

FILE_PATH = os.path.dirname(os.path.realpath(__file__)) + '/version.txt'

class ConnectNGame:
    '''
    Main module class used Connect-N game.
    https://github.com/Kartikei-12/Connect-N
    '''
    is_over = False    
    __version__ = '0.1d.'

    def __init__(self, num_rows = ROWS, num_col = COLUMNS, n = N):
        '''
        Instantiate function for class ConnectNGame
        '''
        for var in [num_rows, num_col, n]:
            if not isinstance(var, int):
                raise ValueError(
                    "Expected <class 'int'> not {0}"\
                        .format(type(var))
                )

        self.__version__ += getVersion(FILE_PATH)

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
