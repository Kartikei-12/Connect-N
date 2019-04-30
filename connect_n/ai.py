"""ai.py

File defining AI for the Connect-N Game
"""
# Python module(s)
import random

# User module(s)
from env import UNIT_SCORE


class AI:
    """class defining AI for the game
    Args:
        game (ConnectNGame): Game object"""

    def __init__(self, game, p_id=1):
        """Instantiate Method"""
        self.p_id = p_id
        self.name = "AI"

        self.game = game
        self.n = game.n
        self.rows = game.rows
        self.cols = game.cols

    def get_move(self):
        """Simple method to fetch AI move
        Note:
            Currently no actual AI or machine learing implementation, just random guesses

        Returns:
            int : Most optimal move (- 1 evan no proper move possible.)"""
        valid_loction = self.game.get_valid_moves()
        if len(valid_loction) == 0:
            return -1
        max_score = -(10 ** 8)  # Really low number
        best_move = random.choice(valid_loction)
        for col in valid_loction:
            temp_board = self.game.board.copy()
            self.game.make_move(col, self.p_id, temp_board)
            if max_score < self.score(temp_board, self.p_id):
                max_score = self.score(temp_board, self.p_id)
                best_move = col
        return best_move

    def string_score(self, string, pid):
        """Calculates score for a player from given string

        Args:
            string (str): Input string
            pid (int): ID of player

        Returns:
            int : Score of the given string"""
        if str(pid) not in string:
            return 0
        else:
            pid = str(pid)

        score = 0
        for begin in range(len(string) - self.n + 1):
            end = min(begin + self.n, len(string))
            for j in range(self.n, 1, -1):
                # Only Me
                if (
                    string[begin:end].count("0") == (self.n - j)
                    and string[begin:end].count(pid) == j
                ):
                    score += (j ** 2) * UNIT_SCORE
                    break
                # Me and Someone else
                if (
                    string[begin:end].count("0") != (self.n - j)
                    and string[begin:end].count(pid) == j
                ):
                    score += (j ** 2) * UNIT_SCORE * (-1.5)
                    break
                # Only Others
                if (
                    string[begin:end].count("0") == (self.n - j)
                    and string[begin:end].count(pid) != j
                ):
                    score += (j ** 2) * UNIT_SCORE * (1.2)
                    break
        return score

    def score(self, board, pid):
        """Calculated Score of board for given player.
        Args:
            pid (int): ID of player

        Returns:
            float : Score of the board for given pid"""
        score = 0
        # Horizontal
        for i in range(self.rows):
            score += self.string_score("".join(str(j) for j in board[i][...]), pid)
        # Vertical
        for i in range(self.cols):
            score += self.string_score("".join(str(j) for j in board[..., i]), pid)
        # Positive Digonal Along Rows
        for i in range(self.n - 1, self.cols):
            score += self.string_score(
                "".join(str(board[j][i - j]) for j in range(min(i + 1, self.rows))), pid
            )
        # Positive Digonal Along Columns
        for i in range(1, self.rows - self.n + 1):
            score += self.string_score(
                "".join(
                    str(board[j + i][self.cols - j - 1]) for j in range(self.rows - i)
                ),
                pid,
            )
        # Negative Digonal Along Rows
        for i in range(self.cols - self.n + 1):
            score += self.string_score(
                "".join(
                    str(board[j][i + j]) for j in range(min(self.rows, self.cols - i))
                ),
                pid,
            )
        # Negative Digonal Along Columns
        for i in range(1, self.rows - self.n + 1):
            score += self.string_score(
                "".join(str(board[i + j][j]) for j in range(self.rows - i)), pid
            )
        return score

    def __str__(self):
        """String representation."""
        return "<class 'AI'> {}".format(self.p_id)
