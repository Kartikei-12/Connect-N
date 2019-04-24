"""
@author: Kartikei Mittal

@email: kartikeimittal@gmail.com

connect_n.py file

Contains main module of this repositry.

https://github.com/Kartikei-12/Connect-N
"""

__author__ = "Kartikei Mittal"

# Python module(s)
import os
import sys
import random
import numpy as np

# User module(s)
from .ai import AI
from .player import Player
from .utility import getVersion
from .pygame_utility import PygameUtility

# Environment Variables
from env import N, ROWS, COLUMNS

FILE_PATH = os.path.dirname(os.path.realpath(__file__)) + "/version.txt"


class ConnectNGame:
    """
    Main module class used Connect-N game.
    
    Args:
        ai (bool): Wheather to play against AI
        graphic (bool): Wheather to play in GUI
        n (int): Number of coins required in a line to win.
        num_rows (int): Number of rows
        num_col (int): Number of columns
    
    Raises:
        TypeError: Expected 'int' for num_rows, num_col, n 
        TypeError: Expected 'bool' for ai, graphic
        ValueError: Argument [num_rows, num_col, n] needs to be positive.
        ValueError: No winning combination possible in [num_rows, num_col, n].
    """

    __version__ = "0.1d."

    def __init__(self, ai=False, graphic=False, n=N, num_rows=ROWS, num_col=COLUMNS):
        """Instantiate function for class ConnectNGame"""

        # Checking 'bool' argument
        for var in [ai, graphic]:
            if not isinstance(var, bool):
                raise TypeError("Expected 'bool' not {0}.".format(type(var)))
        # Checking 'int' argument
        for var in [num_rows, num_col, n]:
            if not isinstance(var, int):
                raise TypeError("Expected 'int' not {0}".format(type(var)))
            elif var < 1:
                raise ValueError("All argument needs to be positive.")
        if num_rows < n and num_col < n:
            raise ValueError("No winning combination possible.")

        self.winner = None
        self.sequence = list()
        self.players = list()

        self.__version__ += getVersion(FILE_PATH)
        self.n = n
        self.rows = num_rows
        self.cols = num_col

        self.GamUtil = None
        self.board = np.zeros((self.rows, self.cols), dtype=int)
        self.play = self.cmd_line

        if ai:
            self.players.append(AI(n, num_rows, num_col))
        if graphic:
            try:
                self.GamUtil = PygameUtility(num_rows, num_col)
            except EnvironmentError as e:
                print(e)
            else:
                self.play = self.graphic

    def get_sequence(self):
        """Sequence of Moves.

        Returns:
            list : Provides sequence of moves by players in the current game till now."""
        return self.sequence

    def simulate(self, sequence):
        """This method simulate a game from list of integers passed,
        each element representing column choosen by corresponding player to make move,
        Useful for trainning of AI.

        Note:
            * As soon as an invalid move is encountered game is aborted,
            * Index of cloumns belong to [0, self.cols), for example if self.cols is 6 column will to 0 to self.cols-1, limits included.
        
        Returns:
            list : Refer self.sequence(same as .get_sequence)."""
        turn = 0
        for col in sequence:
            if self.is_valid_move(col):
                row = self.make_move(col, turn + 1)
            else:
                break
            if self.is_winning_move(row, col):
                self.winner = self.players[turn]
                break
            turn = (turn + 1) % len(self.players)
        return self.sequence

    def reset(self):
        """Resets th game for a new run.
        Note:
            Does NOT removes players from the game."""
        self.winner = None
        self.sequence = list()
        self.board = np.zeros((self.rows, self.cols), dtype=int)

    def add_player(self, p):
        """Method to add players to the game.
    
        Args:
            p (Player): player object
    
        Raises:
            TypeError: "Expected 'Player' not {0}".format(type(p))
            ValueError: '{} already in game.'.format(p)
        """
        if not isinstance(p, Player):
            raise TypeError("Expected 'Player' not {0}".format(type(p)))
        if p.id in [pi.id for pi in self.players] or p.name in [
            pi.name for pi in self.players
        ]:
            raise ValueError("{} already in game.".format(p))
        self.players.append(p)

    def print_board(self):
        """Prints the board on console."""
        print(np.flip(self.board, 0))

    def make_move(self, col, id):
        """Method to make move, returns row in which move was made
    
        Args:
            col (int): Column to insert coin in
            id (int): Id of player making the move
    
        Returns:
            int : Row in which move was made
        """
        self.sequence.append(col)
        for row in range(self.rows):
            if self.board[row][col] == 0.0:
                self.board[row][col] = id
                return row

    def is_valid_move(self, col):
        """Check validity of move, also appends move to 'sequence' list.
        Note:
            -1 is appended to sequence if in valid move
    
        Args:
            col (int): Checks if move can be made in this column
    
        Returns:
            bool True if valid move False otherwise
        """
        if col >= self.cols or self.board[self.rows - 1][col] != 0:
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
            raise ValueError("Testing Empty slot in board.")
        desired_pat = "".join(str(self.board[row][col]) for i in range(self.n))

        # Horizontal Check
        if desired_pat in "".join(
            str(self.board[row][i])
            for i in range(max(0, col - self.n + 1), min(col + self.n, self.cols))
        ):
            return True

        # Vertical Check
        if desired_pat in "".join(
            str(self.board[i][col])
            for i in range(max(0, row - self.n + 1), min(row + self.n, self.rows))
        ):
            return True
        # Positive digonal Check
        if desired_pat in "".join(
            str(self.board[row + i][col + i])
            for i in range(-1 * (self.n - 1), self.n)
            if (row + i) >= 0
            and (col + i) >= 0
            and (row + i) < self.rows
            and (col + i) < self.cols
        ):
            return True
        # Negative digonal Check
        if desired_pat in "".join(
            str(self.board[row - i][col + i])
            for i in range(-1 * (self.n - 1), self.n)
            if (row - i) >= 0
            and (col + i) >= 0
            and (row - i) < self.rows
            and (col + i) < self.cols
        ):
            return True

    def cmd_line(self):
        """Method to play the game in command line."""
        turn = random.randint(0, len(self.players) - 1)
        while True:
            col = self.players[turn].get_move()
            if col == -1:
                continue
            if self.is_valid_move(col):
                row = self.make_move(col, self.players[turn].id)
                if self.is_winning_move(row, col):
                    self.winner = self.players[turn]
                    print("Winner: Player", self.winner.name)
                    return
            else:
                print("Invalid move column already filled, aborting turn!")
            turn = (turn + 1) % len(self.players)
            self.print_board()

    def graphic(self):
        """Method to play the game in GUI using pygame
        
        Note:
            When playing with AI a mouse click is required to trigger AI move"""
        if not self.GamUtil:
            self.cmd_line()
            return
        turn = random.randint(0, len(self.players) - 1)
        while True:
            self.GamUtil.draw(self.board)
            for event in self.GamUtil.get_event():
                if self.GamUtil.is_quit_event(event):
                    sys.exit()

                if self.GamUtil.is_mouse_motion(event):
                    self.GamUtil.draw_black_rec()
                    self.GamUtil.draw_player_coin(self.players[turn].id, event)
                self.GamUtil.update()

                if self.GamUtil.is_mouse_down(event):
                    self.GamUtil.draw_black_rec()
                    if self.players[turn].name == "AI":
                        col = self.players[turn].get_move()
                    else:
                        col = self.GamUtil.get_col(event)

                    if self.is_valid_move(col):
                        row = self.make_move(col, self.players[turn].id)
                        if self.is_winning_move(row, col):
                            self.winner = self.players[turn]
                            self.GamUtil.blit(
                                "Player {} Wins!!".format(self.winner.name),
                                self.winner.id,
                            )
                            self.GamUtil.draw(self.board)
                            self.GamUtil.wait()
                            return
                    turn = (turn + 1) % len(self.players)

    def __str__(self):
        """Representation format:
            <class 'ConnectNGame', NUMBER_OF_ROWS NUMBER_OF_COLUMNS CONNECT_LENGTH>"""
        return "<class 'ConnectNGame', {1} {2} {3} >".format(
            self.rows, self.cols, self.n
        )
