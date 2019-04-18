"""@author: Kartikei Mittal

Unit tests file for current project."""
# Python module(s)
import sys
import unittest

# User module(s)
from default_variables import *
from connect_n.utility import getVersion
from connect_n.player import Player
from connect_n.connect_n import ConnectNGame


class ConnectNTests(unittest.TestCase):
    # Tests for project Connect-N.
    def setUp(self):
        # Tests Set Up
        self.game = ConnectNGame(3, 3, 3)

    def tearDown(self):
        # Tests tear down
        del self.game

    def test_init(self):
        """Testing instantiateing module"""
        self.assertEqual(self.game.num_col, 3)
        self.assertEqual(self.game.num_rows, 3)
        self.assertEqual(self.game.n, 3)

    def test_version(self):
        """Testing version system"""
        self.assertEqual(getVersion("connect_n/version.txt"), self.game.__version__[5:])

    def test_horizontal_winning_move(self):
        """Testing Winning move(Horizontal Check)"""
        self.game.board = [[1.0, 1.0, 1.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]]
        self.assertTrue(self.game.is_winning_move(0, 2))

    def test_vertical_winning_move(self):
        """Testing Winning move(Vertical Check)"""
        self.game.board = [[1.0, 0.0, 0.0], [1.0, 0.0, 0.0], [1.0, 0.0, 0.0]]
        self.assertTrue(self.game.is_winning_move(2, 0))

    def test_positive_digonal_winning_move(self):
        """Testing Winning move(Positive digonal Check)"""
        self.game.board = [[1.0, 2.0, 2.0], [0.0, 1.0, 2.0], [0.0, 0.0, 1.0]]
        self.assertTrue(self.game.is_winning_move(1, 1))

    def test_negative_digonal_winning_move(self):
        """Testing Winning move()"""
        self.game.board = [[1.0, 2.0, 1.0], [2.0, 1.0, 0.0], [1.0, 0.0, 0.0]]
        self.assertTrue(self.game.is_winning_move(1, 1))

    def test_add_player(self):
        """Testing add player method"""
        p = Player("A")
        with self.assertRaises(ValueError):
            self.game.add_player(p)
            self.game.add_player(p)


if __name__ == "__main__":
    """Test Runner"""
    unittest.main(verbosity=3)
