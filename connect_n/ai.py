"""ai.py

File defining AI for the Connect-N Game"""
# Python module(s)
import random

# User module(s)
from env import UNIT_SCORE, OFFSET, LARGE_VALUE, SMALL_VALUE


class AI:
    """class defining AI for the game
    Args:
        p_id (int): ID for AI(default: 1)
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
        if len(valid_loction) == 0:  # No valid moves
            return -1
        max_score = SMALL_VALUE
        best_move = random.choice(valid_loction)
        for col in valid_loction:
            temp_board = self.game.board.copy()
            self.game.make_move(col, self.p_id, temp_board)
            if max_score < self.score(temp_board, self.p_id):
                max_score = self.score(temp_board, self.p_id)
                best_move = col
        return best_move

    def get_move2(self):
        """"""
        pass

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
        score = OFFSET
        for begin in range(len(string) - self.n + 1):
            end = begin + self.n
            zeros = string[begin:end].count("0")
            me = string[begin:end].count(pid)
            other = self.n - zeros - me
            score += UNIT_SCORE * (zeros ** 4 + (me ** 4) * 3 + (other ** 4) * (-2.5))
        return score

    def score(self, board, pid):
        """Calculated Score of board for given player.
        Args:
            board (numpy.ndarray): A 2-D int numpy array representing current state of game
            pid (int): ID of player

        Returns:
            float : Score of the board for given pid"""
        return sum(
            self.string_score(string, pid) for string in self.game.get_strings(board)
        )

    def __str__(self):
        """String representation."""
        return "<class 'AI'> {}".format(self.p_id)
