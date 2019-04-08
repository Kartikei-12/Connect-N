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

        if num_rows < n and num_col < n:
            raise ValueError('No winning combination possible in fiven confirigation.')

        self.winner = None
        self.players = list()
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

    def print_players(self):
        for p in self.players:
            print(p)

    def print_board(self):# *************************************************************
        # Helper function which prints the board
        print(np.flip(self.board, 0))

    def make_move(self, col, id):
        for i in range(self.num_rows):
            if self.board[i][col] == 0:
                self.board[i][col] = id
                return i

    def is_valid_move(self, col):
        if col >= self.num_col or self.board[self.num_rows-1][col] != 0:
            return False
        return True

    def is_winning_move(self, row, col):
        p = str(self.board[row][col])
        desired_pat = "".join(p for i in range(self.n))

        # Horizontal Check
        meaningful_length = ''
        for i in range(max(0, col-self.n+1), min(col+self.n, self.num_col)):
            meaningful_length += str(int(self.board[row][i]))
        if desired_pat in meaningful_length:
            return True
        # Vertical Check
        meaningful_length = ''
        for i in range(max(0, row-self.n+1), min(row+self.n, self.num_rows)):
            meaningful_length += str(int(self.board[i][col]))
        if desired_pat in meaningful_length:
            return True
        

    def play_game(self):# *************************************************************
        turn = len(self.players) - 1
        while not self.is_over:
            turn = (turn+1) % len(self.players)
            try:
                msg = 'Player {0} make your move: '.format(self.players[turn].name)
                col = int(input(msg))-1
            except ValueError as e:
                print(e, 'Aborting current turn, moving ahead.')
                continue
            if self.is_valid_move(col):
                row = self.make_move(col, self.players[turn].id)
                if self.is_winning_move(row, col):
                    self.winner = self.players[turn]
                    self.is_over = True
            else:
                print('Invalid move column filled, aborting turn!')
            self.print_board()
        print(self.winner)

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

