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
from .player import Player
from .utility import getVersion
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
        for var in [num_rows, num_col, n]:
            if not isinstance(var, int):
                raise TypeError(
                    "Expected <class 'int'> not {0}"\
                        .format(type(var))
                )
        self.players = []
        self.is_over = False
        self.__version__ += getVersion(FILE_PATH)

        self.n = n
        self.num_rows = num_rows
        self.num_col = num_col
        self.board = np.zeros((self.num_rows, self.num_col))

    def add_player(self, p):
        if not isinstance(p, Player):
            raise TypeError("Expected <class 'Player'> not {0}".format(type(p)))
        for pi in self.players:
            if p.id == pi.id:
                raise ValueError('{} already in game.'.format(p))
        self.players.append(p)

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

