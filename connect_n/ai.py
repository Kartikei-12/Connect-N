"""ai.py

File defining AI for the Connect-N Game"""

# Python module(s)
import math
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

    def greedy(self):
        """Simple method to fetch AI move, Uses scoring method to determine highest ranking move(greddy approach)

        Returns:
            int : Most optimal move (None if no legal moves)"""
        valid_loction = self.game.get_valid_moves()
        if len(valid_loction) == 0:  # No valid moves
            return None
        max_score = SMALL_VALUE
        best_move = random.choice(valid_loction)
        for col in valid_loction:
            temp_board = self.game.board.copy()
            self.game.make_move(col, self.p_id, temp_board)
            if max_score < self.score(temp_board, self.p_id):
                max_score = self.score(temp_board, self.p_id)
                best_move = col
        return best_move

    def get_move(self):
        """Fetches AI  move

        Returns:
            int : Most optimal move (None if no legal moves)"""
        if len(self.game.get_valid_moves()) == 0:
            return None
        # Check if AI winning, and win
        col = self.game.is_p_id_winning(self.p_id)
        if col:
            return col  # Retuen only if non None value returned

        try:  # Checks if next player is known, if not known finds out
            a = self.next_player.p_id
        except AttributeError:
            i = 0
            self.next_player = self.game.players[0]
            for p in self.game.players:
                if p.p_id == 1:
                    break
                i += 1
            if i < len(self.game.players):
                self.next_player = self.game.players[i + 1]
        else:
            del a

        # Check if next player is winning, and stop him/her
        col = self.game.is_p_id_winning(self.next_player.p_id)
        if col:
            return col

        return self.minmax(
            self.game.board.copy(), self.n + 1, -math.inf, math.inf, True
        )[0]

    def minmax(self, board, depth, alpha, beta, maximizingPlayer):
        """MinMax algortihm for AI implementation

        Args:
            board (numpu.ndarray): 2-D numpy array representing board in which game is being played
            depth (int): Depth upto which to look
            alpha (int): Parameter for alpha-beta purning
            beta (int): Parameter for alpha-beta purning
            maximizingPlayer (bool): Wheather maximizing player or not

        Returns:
            tuple : 2 length tuple, first element column, second score"""
        if self.game.is_p_id_winning(self.p_id, board):
            return (None, LARGE_VALUE)
        if self.game.is_p_id_winning(self.next_player.p_id, board):
            return (None, SMALL_VALUE)
        if len(self.game.get_valid_moves(board)) == 0:
            return (None, 0)
        if depth == 0:
            return (None, self.score(board, self.p_id))

        value = math.inf
        p_id = self.next_player.p_id
        column = random.choice(self.game.get_valid_moves(board))
        if maximizingPlayer:
            value = -math.inf
            p_id = self.p_id

        for col in self.game.get_valid_moves(board):
            b_copy = board.copy()
            row = self.game.make_move(col, p_id, b_copy)
            new_score = self.minmax(
                b_copy, depth - 1, alpha, beta, not maximizingPlayer
            )[1]
            if maximizingPlayer:
                if new_score > value:
                    value = new_score
                    column = col
                alpha = max(alpha, value)
            else:
                if new_score < value:
                    value = new_score
                    column = col
                beta = min(beta, value)
            if alpha >= beta:
                break
        del row
        return (column, value)

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
