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

    def string_score(self, string, id):
        """Calculates score for a player from given string

        Args:
            string (str): Input string
            id (int): ID of player"""
        if str(id) not in string:
            return 0
        elif id == -1:
            id = "#"
            string = string.replace("-1", "#")
        else:
            id = str(id)

        score = 0
        for begin in range(len(string) - self.n + 1):
            end = min(begin + self.n, len(string))
            for j in range(self.n - 1, 1, -1):
                if string[begin:end].count(id) == j and string[begin:end].count(
                    "0"
                ) == (self.n - j):
                    score += j * UNIT_SCORE
                    break
        return score

    def score(self, board, id):
        """Calculated Score of board for given player.
        Args:
            id (int): ID of player"""
        score = 0
        # Horizontal
        for i in range(self.rows):
            score += self.string_score("".join(str(j) for j in board[i][...]), id)
        # Vertical
        for i in range(self.cols):
            score += self.string_score("".join(str(j) for j in board[..., i]), id)
        # Positive Digonal Along Rows
        for i in range(self.n - 1, self.cols):
            score += self.string_score(
                "".join(str(board[j][i - j]) for j in range(min(i + 1, self.rows))), id
            )
        # Positive Digonal Along Columns
        for i in range(1, self.rows - self.n + 1):
            score += self.string_score(
                "".join(
                    str(board[j + i][self.cols - j - 1]) for j in range(self.rows - i)
                ),
                id,
            )
        # Negative Digonal Along Rows
        for i in range(self.cols - self.n + 1):
            score += self.string_score(
                "".join(
                    str(board[j][i + j]) for j in range(min(self.rows, self.cols - i))
                ),
                id,
            )
        # Negative Digonal Along Columns
        for i in range(1, self.rows - self.n + 1):
            score += self.string_score(
                "".join(str(board[i + j][j]) for j in range(self.rows - i)), id
            )
        return score

    def __str__(self):
        """String representation."""
        return "<class 'AI'> {}".format(self.id)
