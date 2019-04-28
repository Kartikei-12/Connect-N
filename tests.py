"""@author: Kartikei Mittal

Unit tests file for current project."""

# Python module(s)
import sys
import unittest
import numpy as np
import HtmlTestRunner

# User module(s)
from env import UNIT_SCORE
from utility import update_readme

# Project module(s)
from connect_n.ai import AI
from connect_n.utility import getVersion
from connect_n.player import Player
from connect_n.connect_n import ConnectNGame


class ConnectNTests(unittest.TestCase):
    # Tests for project Connect-N.
    def setUp(self):
        """setUp"""
        self.game = ConnectNGame(n=3, num_col=3, num_rows=3, ai=False)

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
        self.game.simulate([0, 1, 0, 1, 0])
        self.assertTrue(self.game.winner)
        self.assertEqual(self.game.winner.name, self.game.players[0].name)

    def test_make_move(self):
        """Testing make move method"""
        p = Player("A")
        self.game.add_player(p)
        self.assertEqual(self.game.make_move(0, p.id), 0)
        p = Player("B")
        self.game.add_player(p)
        self.assertEqual(self.game.make_move(0, p.id), 1)

    def test_is_valid_move(self):
        """Testing is_valid_move"""
        p = Player("A")
        self.game.add_player(p)
        self.assertTrue(self.game.is_valid_move(0))
        self.game.board = [[1, 0, 0], [1, 0, 0], [1, 0, 0]]
        self.assertFalse(self.game.is_valid_move(0))


class AITests(unittest.TestCase):
    # Tests for project Connect-N.
    def setUp(self):
        """setUp"""
        self.ai = AI(ConnectNGame(ai=False, graphic=False))

    def tearDown(self):
        """tearDown"""
        del self.ai

    def test_string_score(self):
        """Testing string_score method"""
        self.assertEqual(self.ai.string_score("11011", 1), UNIT_SCORE * 18)

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
        self.assertEqual(UNIT_SCORE * 16, self.ai.score(board, 1))

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
        self.assertEqual(UNIT_SCORE * 17, self.ai.score(board, 1))

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
        self.assertEqual(UNIT_SCORE * 18, self.ai.score(board, 1))

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
        self.assertEqual(UNIT_SCORE * 13, self.ai.score(board, 1))


if __name__ == "__main__":
    """Test Runner"""

    # Seprating coustom arguments from mormal unittest argument
    argv_tpl = ("--update-readme",)  # Expected coustom arguments
    del_lst = []
    coustom_argv = [sys.argv[0]]
    for i, argv in enumerate(sys.argv):
        if argv in argv_tpl:
            del_lst.append(i)
            coustom_argv.append(argv)
    del_lst.reverse()  # Faster deletion when deleting higher index element first
    for i in del_lst:
        del sys.argv[i]

    testRunner = HtmlTestRunner.HTMLTestRunner(
        verbosity=3,
        descriptions=False,
        open_in_browser=False,
        combine_reports=True,
        report_name="test_result",
        add_timestamp=False,
    )
    unittest.main(testRunner=testRunner, exit=False)

    if len(coustom_argv) > 1 and coustom_argv[1] == "--update-readme":
        update_readme()

    print("Done")
