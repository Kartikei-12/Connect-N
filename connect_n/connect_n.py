"""@author: Kartikei Mittal

@email: kartikeimittal@gmail.com

connect_n.py file

Contains main module of this repositry.

https://github.com/Kartikei-12/Connect-N"""


# Python module(s)
import os
import random
import numpy as np

# User module(s)
from .ai import AI
from .player import Player
from .pygame_utility import PygameUtility
from .utility import getVersion, recordGame, dummy_method

# Environment Variables
from env import N, ROWS, COLUMNS


class ConnectNGame:
    """Main module class used Connect-N game.

    Args:
        ai (bool): Enable/Disable AI
        web (bool): Web Interface
        record (bool): Enable game recording.
        graphic (bool): GUI(true) or command line interface(false)
        n (int): Number of coins required in a line to win.
        num_rows (int): Number of rows
        num_col (int): Number of columns

    Raises:
        TypeError: Expected 'int' for num_rows, num_col, n
        TypeError: Expected 'bool' for ai, graphic, web, record
        ValueError: Argument [num_rows, num_col, n] needs to be positive
        ValueError: No winning combination possible in [num_rows, num_col, n]"""

    __version__ = "0.1d."

    def __init__(
        self,
        ai=True,
        web=False,
        record=False,
        graphic=True,
        n=N,
        num_rows=ROWS,
        num_col=COLUMNS,
    ):
        """Instantiate function for class ConnectNGame"""

        # Checking 'bool' argument
        for var in (ai, graphic, web, record):
            if not isinstance(var, bool):
                raise TypeError("Expected 'bool' not {0}.".format(type(var)))
        # Checking 'int' argument
        for var in (n, num_rows, num_col):
            if not isinstance(var, int):
                raise TypeError("Expected 'int' not {0}".format(type(var)))
            elif var < 1:
                raise ValueError("All argument needs to be positive.")
            elif var < n:
                raise ValueError("No winning combination possible")

        PATH = os.path.dirname(os.path.realpath(__file__))
        FILE_PATH = PATH + "/version.txt"
        self.__version__ += getVersion(FILE_PATH)

        self.winner = None
        self.GUIUtil = None
        self.sequence = list()
        self.players = list()

        self.n = n
        self.rows = num_rows
        self.cols = num_col

        self.board = np.zeros((self.rows, self.cols), dtype=int)

        self.play = self.cmd_line
        self.record_game = dummy_method

        if ai:
            self.players.append(AI(self))
        if record:
            self.record_game = recordGame
        if graphic:
            try:
                self.GUIUtil = PygameUtility(num_rows, num_col)
            except EnvironmentError as e:
                print(e)
            else:
                self.play = self.graphic

    def simulate(self, turn, sequence):
        """This method simulate a game from list of integers passed, each element representing column choosen by corresponding player to make move, Useful for trainning of AI.

        Note:
            * As soon as an invalid move is encountered game is aborted,
            * Index of cloumns belong to [0, self.cols), for example if self.cols is 6 column will to 0 to self.cols-1, limits included.

        Args:
            turn (int): Index of player from self.players list who gets the first turn
            sequence (list): List of moves by player in order of thir occurence in self.players list

        Returns:
            list : Refer self.sequence"""
        for col in sequence:
            if self.is_valid_move(col):
                row = self.make_move(col, self.players[turn].p_id)
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
            Does NOT removes players from the game"""
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
        if p.p_id in [player.p_id for player in self.players]:
            raise ValueError("{} already in game.".format(p))
        self.players.append(p)

    def is_p_id_winning(self, p_id, board=None):
        """"""
        if board is None:
            board = self.board
        for col in self.get_valid_moves(board):
            board_copy = board.copy()
            row = self.make_move(col, p_id, board_copy)
            if self.is_winning_move(row, col, board_copy):
                return col
        return None

    def print_board(self):
        """Prints the board on console"""
        print(np.flip(self.board, 0))  # 0: Vertical flip

    def make_move(self, col, p_id, board=None):
        """Method to make move, returns row in which move was made

        Args:
            col (int): Column to insert coin in
            p_id (int): Id of player making the move
            board (numpy.ndarray): 2-D numpy array representing board in which game is being played

        Returns:
            int : Row in which move was made"""
        if board is None:
            board = self.board
            self.sequence.append(col)
        for row in range(self.rows):
            if board[row][col] == 0:
                board[row][col] = p_id
                return row
        return None

    def get_valid_moves(self, board=None):
        """Valid Moves

        Args:
            board (numpy.ndarray): 2-D numpy array representing board in which game is being played

        Returns:
            list : List of all valid moves"""
        if board is None:
            board = self.board
        return [i for i in range(self.cols) if self.is_valid_move(i, board)]

    def is_valid_move(self, col, board=None):
        """Check validity of move

        Args:
            col (int): Checks if move can be made in this column
            board (numpy.ndarray): 2-D numpy array representing board in which game is being played

        Returns:
            bool : True if valid move False otherwise"""
        if board is None:
            board = self.board
        if col < 0 or col >= self.cols or board[self.rows - 1][col] != 0:
            return False
        return True

    def is_winning_move(self, row, col, board=None):
        """Method to check for winning move,

        Note:
            Board is displayed in flipped position so,
            What appears to positive digonal is actually negative digonal,
            and vice versa.

        Args:
            row (int): Row in which last move was made
            col (int): Column in which last move was made
            board (numpy.ndarray): 2-D numpy array representing board in which game is being played

        Returns:
            bool : True if given position enabled a winning move"""
        if board is None:
            board = self.board
        if board[row][col] == 0:
            raise ValueError("Testing Empty slot in board.")
        desired_pat = "".join(str(board[row][col]) for i in range(self.n))

        # Horizontal Check
        if desired_pat in "".join(
            str(board[row][i])
            for i in range(max(0, col - self.n + 1), min(col + self.n, self.cols))
        ):
            return True

        # Vertical Check
        if desired_pat in "".join(
            str(board[i][col])
            for i in range(max(0, row - self.n + 1), min(row + self.n, self.rows))
        ):
            return True
        # Positive digonal Check
        if desired_pat in "".join(
            str(board[row + i][col + i])
            for i in range(-1 * (self.n - 1), self.n)
            if (row + i) >= 0
            and (col + i) >= 0
            and (row + i) < self.rows
            and (col + i) < self.cols
        ):
            return True
        # Negative digonal Check
        if desired_pat in "".join(
            str(board[row - i][col + i])
            for i in range(-1 * (self.n - 1), self.n)
            if (row - i) >= 0
            and (col + i) >= 0
            and (row - i) < self.rows
            and (col + i) < self.cols
        ):
            return True

    def get_strings(self, board=None):
        """Method generates all string of 'n' length from board

        Args:
            board (numpy.ndarray): A 2-D int numpy array representing current state of game

        Returns:
            list : A list of strings which may have any significance in the game"""
        strings = list()
        if board is None:
            board = self.board
        # Horizontal
        for i in range(self.rows):
            strings.append("".join(str(j) for j in board[i][...]))
        # Vertical
        for i in range(self.cols):
            strings.append("".join(str(j) for j in board[..., i]))
        # Positive Digonal Along Rows
        for i in range(self.n - 1, self.cols):
            strings.append(
                "".join(str(board[j][i - j]) for j in range(min(i + 1, self.rows)))
            )
        # Positive Digonal Along Columns
        for i in range(1, self.rows - self.n + 1):
            strings.append(
                "".join(
                    str(board[j + i][self.cols - j - 1]) for j in range(self.rows - i)
                )
            )
        # Negative Digonal Along Rows
        for i in range(self.cols - self.n + 1):
            strings.append(
                "".join(
                    str(board[j][i + j]) for j in range(min(self.rows, self.cols - i))
                )
            )
        # Negative Digonal Along Columns
        for i in range(1, self.rows - self.n + 1):
            strings.append("".join(str(board[i + j][j]) for j in range(self.rows - i)))
        return strings

    def cmd_line(self):
        """Method to play the game in command line"""
        turn = random.randint(0, len(self.players) - 1)
        while True:
            self.print_board()
            col = self.players[turn].get_move()
            if self.is_valid_move(col):
                row = self.make_move(col, self.players[turn].p_id)
                if self.is_winning_move(row, col):
                    self.winner = self.players[turn]
                    print("Winner: ", self.winner.name)
                    break
            else:
                print("Invalid move column already filled, aborting turn!")
            turn = (turn + 1) % len(self.players)
        self.record_game(self)

    def graphic(self):
        """Method to play the game in GUI using pygame"""
        if len(self.players) > 3:  # TODO: Remove magic number
            print("GUI currently only support 3 players.")
            self.cmd_line()
            return
        self.winner = self.GUIUtil.play(
            self.board,
            self.players,
            self.is_valid_move,
            self.make_move,
            self.is_winning_move,
        )
        self.record_game(self)

    def __str__(self):
        """Representation format:
            <class 'ConnectNGame', NUMBER_OF_ROWS NUMBER_OF_COLUMNS CONNECT_LENGTH>"""
        return "<class 'ConnectNGame', {0} {1} {2} >".format(
            self.rows, self.cols, self.n
        )
