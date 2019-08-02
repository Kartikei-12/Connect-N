"""AI Tests"""

# Python module(s)
import unittest
import numpy as np

# User module(s)
from env import UNIT_SCORE, OFFSET

# Project module(s)
from connect_n.ai import AI
from connect_n.player import Player
from connect_n.connect_n import ConnectNGame

class AITests(unittest.TestCase):
    """Tests for project Connect-N"""

    def setUp(self):
        """setUp"""
        self.ai = AI(ConnectNGame(ai=True, graphic=False))

    def tearDown(self):
        """tearDown"""
        del self.ai

    def test_string_score(self):
        """Testing string_score method"""
        self.assertEqual(self.ai.string_score("11011", 1), UNIT_SCORE * 488 + OFFSET)

    def test_horizontal_score(self):
        """Testing horizontal_score"""
        board = np.array(
            [
                [0, 1, 1, 0, 0, 1, 1],
                [0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0],
            ],
            dtype=int,
        )
        self.assertEqual(UNIT_SCORE * 4752 + OFFSET, self.ai.score(board, 1))

    def test_vertical_score(self):
        """Testing vertical_score"""
        board = np.array(
            [
                [1, 0, 0, 0, 0, 1, 0],
                [1, 0, 0, 0, 0, 1, 0],
                [0, 0, 0, 0, 0, 1, 0],
                [0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0],
            ],
            dtype=int,
        )
        self.assertEqual(UNIT_SCORE * 4680 + OFFSET, self.ai.score(board, 1))

    def test_positive_digonal_score(self):
        """Testing positive_digonal_score"""
        board = np.array(
            [
                [0, 0, 0, 1, 0, 0, 0],
                [0, 0, 1, 0, 0, 0, 0],
                [0, 1, 0, 0, 0, 0, 1],
                [0, 0, 0, 0, 0, 1, 0],
                [0, 0, 0, 0, 1, 0, 0],
                [0, 0, 0, 0, 0, 0, 0],
            ],
            dtype=int,
        )
        self.assertEqual(UNIT_SCORE * 6462 + OFFSET, self.ai.score(board, 1))

    def test_negative_digonal_score(self):
        """Testing negative_digonal_score"""
        board = np.array(
            [
                [0, 0, 1, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0],
                [1, 0, 0, 0, 0, 0, 1],
                [0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 1, 0, 0],
                [0, 0, 0, 1, 0, 0, 0],
            ],
            dtype=int,
        )
        self.assertEqual(UNIT_SCORE * 5200 + OFFSET, self.ai.score(board, 1))

    def test_greedy(self):
        """Greedy Test"""
        self.ai.game.board = np.array(
            [
                [0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0],
                [1, 0, 0, 0, 0, 0, 0],
                [1, 0, 2, 0, 2, 0, 2],
            ],
            dtype=int,
        )
        self.assertEqual(self.ai.greedy(), 1)

    def test_get_move(self):
        """Greedy Test"""
        self.ai.game.players.append(Player("Rex"))
        self.ai.game.board = np.array(
            [
                [0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0],
                [1, 0, 0, 0, 0, 0, 0],
                [1, 0, 0, 0, 0, 0, 0],
                [1, 0, 2, 0, 2, 0, 2],
            ],
            dtype=int,
        )
        self.assertEqual(self.ai.get_move(), 1)

def main():
    """Test Runner"""
    unittest.main(
        verbosity=3,
        descriptions=False,
        combine_reports=True,
        report_name="../reports/test_result_ai",
        add_timestamp=False,
        exit=False
    )

if __name__ == "__main__":
    main()

