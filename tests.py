"""@author: Kartikei Mittal

Unit tests file for current project."""

# Python module(s)
import sys
import unittest
import HtmlTestRunner

# User module(s)
from utility import update_readme
from default_variables import *
from connect_n.utility import getVersion
from connect_n.player import Player
from connect_n.connect_n import ConnectNGame


class ConnectNTests(unittest.TestCase):
    # Tests for project Connect-N.
    def setUp(self):
        # Tests Set Up
        self.game = ConnectNGame(n=3, num_col=3, num_rows=3)

    def tearDown(self):
        # Tests tear down
        self.game.reset()
        del self.game

    def test_init(self):
        """Testing instantiate module"""
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

    def test_simulate(self):
        """Testing simulate method"""
        self.game.add_player(Player("A"))
        self.game.add_player(Player("B"))
        seq = self.game.simulate([0, 1, 0, 1, 0, 1])
        self.assertTrue(self.game.winner)
        self.assertEqual(self.game.winner, self.game.players[0])

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
        self.game.board = [[1.0, 0.0, 0.0], [1.0, 0.0, 0.0], [1.0, 0.0, 0.0]]
        self.assertFalse(self.game.is_valid_move(0))


if __name__ == "__main__":
    """Test Runner"""
    argv_tpl = ("--update-readme",)
    del_lst = []
    coustom_argv = [sys.argv[0]]
    for i, argv in enumerate(sys.argv):
        if argv in argv_tpl:
            del_lst.append(i)
            coustom_argv.append(argv)

    del_lst.reverse()
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
