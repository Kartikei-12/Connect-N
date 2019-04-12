"""
@author: Kartikei Mittal
@email: kartikeimittal@gmail.com
connect_n.py file
Contains main module of this repositry.
https://github.com/Kartikei-12/Connect-N
"""

__author__ = 'Kartikei Mittal'

# Python module(s)
import os
import sys
import math
import pygame
import numpy as np

# User module(s)
from default_variables import *
from .player import Player
from .utility import getVersion

FILE_PATH = os.path.dirname(os.path.realpath(__file__)) + '/version.txt'

# Pygame setup
# Currently oly works for default board size and upto 3 players.
width = 0
height = 0
pygame.init()
MY_FONT = pygame.font.SysFont("monospace", 75)
width = COLUMNS * SQUARESIZE
height = (ROWS+1) * SQUARESIZE
screen = pygame.display.set_mode((width, height))
pygame.display.update()

class ConnectNGame:
    """
    Main module class used Connect-N game.
    
    Args:
        num_rows (int): Number of rows
        num_col (int): Number of columns
    
    Raises:
        TypeError: "Expected <class 'int'> not {0}".format(type(var))
        ValueError: All argument needs to be positive.
        ValueError: No winning combination possible in fiven confirigation.
    """
    __version__ = '0.1d.'
    
    def __init__(self, num_rows = ROWS, num_col = COLUMNS, n = N):
        """Instantiate function for class ConnectNGame"""
        for var in [num_rows, num_col, n]:
            if not isinstance(var, int):
                raise TypeError(
                    "Expected <class 'int'> not {0}"\
                        .format(type(var))
                )

        if num_rows < 1 or num_col < 1 or m < 1:
            raise ValueError('All argument needs to be positive.')

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
        """Method to add players to the game.
    
        Args:
            p (Player): player object
    
        Raises:
            TypeError: "Expected <class 'Player'> not {0}".format(type(p))
            ValueError: '{} already in game.'.format(p)
        """
        if not isinstance(p, Player):
            raise TypeError("Expected <class 'Player'> not {0}".format(type(p)))
        if p.id in [pi.id for pi in self.players]:
            raise ValueError('{} already in game.'.format(p))
        self.players.append(p)

    def print_board(self):
        """Helper function which prints the board"""
        print(np.flip(self.board, 0))

    def make_move(self, col, id):
        """Method to make move, returns row in which move was made
    
        Args:
            col (int): Column to insert coin in
            id (int): Id of player making the move
    
        Returns:
            int Row in which move was made
        """
        for row in range(self.num_rows):
            if self.board[row][col] == 0.0:
                self.board[row][col] = id
                return row

    def is_valid_move(self, col):
        """Check validity of move
    
        Args:
            col (int): Checks if move can be made in this column
    
        Returns:
            bool True if valid move False otherwise
        """
        if col >= self.num_col or self.board[self.num_rows-1][col] != 0:
            return False
        return True

    def is_winning_move(self, row, col):
        """
        Method to check for winning move,
    
        Note:
            Board is displayed in flipped position so,
            What appears to positive digonal is actually negative digonal,
            and vice versa.
    
        Args:
            row (int): Row in which last move was made.
            col (int): Column in which last move was made.
        """
        if self.board[row][col] == 0.0:
            raise ValueError('Testing Empty slot in board.')
        desired_pat = "".join(str(int(self.board[row][col])) for i in range(self.n))

        # Horizontal Check
        if desired_pat in "".join(
            str(int(self.board[row][i])) for i in \
                range(
                    max(0, col-self.n+1),
                    min(col+self.n, self.num_col)
                )
            ):
            return True
        
        # Vertical Check
        if desired_pat in "".join(
            str(int(self.board[i][col])) for i in \
                range(
                    max(0, row-self.n+1),
                    min(row+self.n, self.num_rows)
                )
            ):
            return True
        # Positive digonal Check
        if desired_pat in "".join(str(int(self.board[row+i][col+i])) for i in 
                range(-1*(self.n-1), self.n) if 
                (row+i)>=0 and (col+i)>=0 and
                (row+i)<self.num_rows and (col+i)<self.num_col):
            return True
        # Negative digonal Check
        if desired_pat in "".join(str(int(self.board[row-i][col+i])) for i in 
                range(-1*(self.n-1), self.n) if 
                (row-i)>=0 and (col+i)>=0 and
                (row-i)<self.num_rows and (col+i)<self.num_col):
            return True
        
    def play_game(self):
        """Method to play the game in command line."""
        pygame.quit()
        num_turn = 0
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
                if num_turn/len(self.players) >= (self.n-1) \
                    and self.is_winning_move(row, col):
                    self.winner = self.players[turn]
                    self.is_over = True
                num_turn += 1
            else:
                print('Invalid move column filled, aborting turn!')
            self.print_board()
        print('Winner: Player', self.winner.name)

    def draw_board(self):
        """Draws game board got pygame"""
        for c in range(self.num_col):
            for r in range(self.num_rows):
                pygame.draw.rect(
                    screen, BLUE,
                    (
                        c*SQUARESIZE, r*SQUARESIZE+SQUARESIZE,
                        SQUARESIZE, SQUARESIZE
                    )
                )
        for c in range(self.num_col):
            for r in range(self.num_rows):
                pygame.draw.circle(
                    screen,
                    C_LIST[int(self.board[r][c])],
                    (
                        int(c*SQUARESIZE+SQUARESIZE/2),
                        height-int(r*SQUARESIZE+SQUARESIZE/2)
                    ), RADIUS
                )
        pygame.display.update()

    def play_game_graphic(self):        
        """Method to play the game in GUI using pygame."""
        turn = 0
        self.draw_board()
        while not self.is_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                
                if event.type == pygame.MOUSEMOTION:
                    pygame.draw.rect(screen, BLACK, (0,0, width, SQUARESIZE))
                    posx = event.pos[0]
                    pygame.draw.circle(
                        screen,
                        C_LIST[turn+1],
                        (
                            posx,
                            int(SQUARESIZE/2)
                        ), RADIUS
                    )
                pygame.display.update()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    pygame.draw.rect(screen, BLACK, (0,0, width, SQUARESIZE))
                    col = int(math.floor(event.pos[0]/SQUARESIZE))

                    if self.is_valid_move(col):
                        row = self.make_move(col, self.players[turn].id)
                        if self.is_winning_move(row, col):
                            self.winner = self.players[turn]
                            label = MY_FONT.render(
                                "Player {}!!".format(self.winner.name),
                                1, C_LIST[turn+1]
                            )
                            screen.blit(label, (40,10))
                            self.is_over = True
                    turn = (turn+1) % len(self.players)
                    self.draw_board()            
        pygame.time.wait(3000)

    def __str__(self):
        """
        Representation format:
            <class 'CLASS NAME', NUMBER_OF_ROWS NUMBER_OF_COLUMNS CONNECT_LENGTH>
        """
        return "<class '{0}', {1} {2} {3} >"\
            .format(
                self.__class__.__name__,
                self.num_rows,
                self.num_col,
                self.n
            )
