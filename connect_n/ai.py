"""ai.py

File defining AI for the Connect-N Game
"""

# Python module(s)
import random

# User module(s)
from env import UNIT_SCORE


class AI:
    """class representing AI in the game
    Args:
        n (int): Number of coins required in a line to win.
        num_rows (int): Number of rows
        num_col (int): Number of columns"""

    def __init__(self, n, rows, cols, id=-1):
        """Instantiate Method"""
        self.id = id
        self.name = "AI"

        self.n = n
        self.rows = rows
        self.cols = cols

    def get_move(self):
        """Simple method to fetch AI move
        Note:
            Currently no actual AI or machine learing implementation, just random guesses."""
        return random.randint(0, self.cols - 1)

    # def string_score(self, string, id):
    #     """Calculates score for a player from given string

    #     Args:
    #         string (str): Input string
    #         id (int): ID of player"""
    #     score = 0
    #     desired_pat = "".join(str(id) for i in range(self.n))
    #     dummy_str = "".join('*' for i in range(self.n))
    #     for i in range(self.n-1, 1, -1):
    #         while len(string) >= i and desired_pat[0:i] in string:
    #             score += i * UNIT_SCORE
    #             string = string.replace(
    #                 desired_pat[0:i],
    #                 dummy_str[0:i], 1 # 1 to replace only first occurence
    #             )
    #     return score

    # def score(self, board, id):
    #     """Calculated Score of board for given player.
    #     Args:
    #         id (int): ID of player"""
    #     score = 0
    #     # Horizontal
    #     for i in range(self.rows):
    #         score += self.string_score(
    #             "".join(
    #                 str(int(j)) for j in board[i][:]
    #             ), id
    #         )
    #     # Vertical
    #     for i in range(self.cols):
    #         score += self.string_score(
    #             "".join(
    #                 str(int(j)) for j in board[:][i]
    #             ), id
    #         )
    #     # Positive Digonal Along Rows
    #     for i in range(self.n - 1, self.rows):
    #         score += self.string_score(
    #             "".join(
    #                 str(int(board[j][i-j])) for j in range(i+1)
    #             ), id
    #         )
    #     # Positive Digonal Along Columns
    #     return score

    def __str__(self):
        """"""
        return "<class 'AI'> {}".format(self.id)
