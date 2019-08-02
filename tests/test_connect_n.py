"""Connect-N Tests"""

# Python module(s)
import unittest
import numpy as np

# Project module(s)
from connect_n.player import Player
from connect_n.utility import getVersion
from connect_n.connect_n import ConnectNGame


class ConnectNTests(unittest.TestCase):
    # Tests for project Connect-N.
    def setUp(self):
        """setUp"""
        self.game = ConnectNGame(n=3, num_col=3, num_rows=3, ai=False, graphic=False)

    def tearDown(self):
        """tearDown"""
        self.game.reset()
        del self.game

    def test_version(self):
        """Testing version system"""
        self.assertEqual(getVersion("connect_n/version.txt"), self.game.__version__[5:])

    def test_horizontal_winning_move(self):
        """Testing Winning move(Horizontal Check)"""
        self.game.board = [[1, 1, 1], [0, 0, 0], [0, 0, 0]]
        self.assertTrue(self.game.is_winning_move(0, 2))
        self.game.board = [[1, 1, 0], [1, 0, 0], [0, 0, 0]]
        self.assertFalse(self.game.is_winning_move(1, 0))
        self.game.board = [[1, 1, 0], [0, 1, 0], [0, 0, 0]]
        self.assertFalse(self.game.is_winning_move(1, 1))

    def test_vertical_winning_move(self):
        """Testing Winning move(Vertical Check)"""
        self.game.board = [[1, 0, 0], [1, 0, 0], [1, 0, 0]]
        self.assertTrue(self.game.is_winning_move(2, 0))
        self.game.board = [[1, 0, 0], [1, 0, 0], [0, 1, 0]]
        self.assertFalse(self.game.is_winning_move(2, 1))
        self.game.board = [[1, 1, 0], [1, 0, 0], [0, 0, 0]]
        self.assertFalse(self.game.is_winning_move(0, 1))

    def test_positive_digonal_winning_move(self):
        """Testing Winning move(Positive digonal Check)"""
        self.game.board = [[1, 2, 2], [0, 1, 2], [0, 0, 1]]
        self.assertTrue(self.game.is_winning_move(1, 1))

    def test_negative_digonal_winning_move(self):
        """Testing Winning move()"""
        self.game.board = [[1, 2, 1], [2, 1, 0], [1, 0, 0]]
        self.assertTrue(self.game.is_winning_move(1, 1))

    def test_add_player(self):
        """Testing add player method"""
        p = Player("A")
        with self.assertRaises(ValueError):
            self.game.add_player(p)
            self.game.add_player(p)

    def test_simulate(self):
        """Testing simulate method"""
        self.game.add_player(Player("A"))
        self.game.add_player(Player("B"))
        self.game.simulate(turn=0, sequence=[0, 1, 0, 1, 0])
        self.assertTrue(self.game.winner)
        self.assertEqual(self.game.winner.name, self.game.players[0].name)

    def test_make_move(self):
        """Testing make move method"""
        p = Player("A")
        self.game.add_player(p)
        self.assertEqual(self.game.make_move(0, p.p_id), 0)
        p = Player("B")
        self.game.add_player(p)
        self.assertEqual(self.game.make_move(0, p.p_id), 1)

    def test_is_valid_move(self):
        """Testing is_valid_move"""
        p = Player("A")
        self.game.add_player(p)
        self.assertTrue(self.game.is_valid_move(0))
        self.game.board = [[1, 0, 0], [1, 0, 0], [1, 0, 0]]
        self.assertFalse(self.game.is_valid_move(0))

    def test_get_valid_moves(self):
        """Testing valid moves"""
        board = [[0, 0, 0], [0, 0, 0], [1, 0, 0]]
        self.assertEqual(self.game.get_valid_moves(board=board), [1, 2])

    def test_get_strings(self):
        """Testing get_strings"""
        board = np.array([[0, 0, 0], [0, 0, 0], [1, 0, 0]], dtype=int)
        strings = ["000", "000", "100", "001", "000", "000", "001", "000"]
        self.assertEqual(self.game.get_strings(board=board), strings)


def main():
    """Test Runner"""
    unittest.main(
        verbosity=3,
        descriptions=False,
        combine_reports=True,
        report_name="../reports/test_result_connect_n",
        add_timestamp=False,
        exit=False,
    )


if __name__ == "__main__":
    main()
