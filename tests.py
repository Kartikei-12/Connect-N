"""@author: Kartikei Mittal

Unit tests file for current project."""

# Python module(s)
import sys
import time
import json
import unittest
import numpy as np
import HtmlTestRunner

# User module(s)
from env import UNIT_SCORE, OFFSET
from utility import update_readme, clear_trailling_space

# Project module(s)
from connect_n.ai import AI
from connect_n.utility import getVersion
from connect_n.player import Player
from connect_n.connect_n import ConnectNGame
from connect_n.api.app import create_app, app, db
from connect_n.api.db_model import User
from connect_n.api.utility import compile_response


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


class PygameUtilityTests(unittest.TestCase):
    # Tests for project Connect-N.
    def setUp(self):
        """setUp"""
        self.game = ConnectNGame(graphic=True, ai=True)

    def tearDown(self):
        """tearDown"""
        self.game.reset()
        del self.game

    def test_play(self):
        """Testing graphic play method"""
        self.game.players.append(AI(self.game, 2))
        self.game.play()
        self.assertEqual(self.game.winner.name, "AI")


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


class UserModelCase(unittest.TestCase):
    """API Database User Model testing"""

    def setUp(self):
        """Setup"""
        self.app = create_app("")
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        """Tear Down"""
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_password_hashing(self):
        """Testing Password hashing"""
        u = User(username="susan")
        u.set_password("cat")
        self.assertFalse(u.check_password("dog"))
        self.assertTrue(u.check_password("cat"))

    def test_check_token(self):
        """Tesing token verification"""
        u = User(username="susan")
        token = u.get_token()
        self.assertIsNotNone(User.check_token(token))
        u.revoke_token()

    def test_token_expiration(self):
        """"""
        u = User(username="susan")
        token = u.get_token(expires_in=1)
        time.sleep(2)
        self.assertIsNone(User.check_token(token))


class APIUtility(unittest.TestCase):
    """API utility method testing"""

    def test_compile_response(self):
        """Testing compile_response"""
        json_str = compile_response(test="test")
        json_dict = json.loads(json_str)
        self.assertEqual(json_dict["test"], "test")
        self.assertEqual(json_dict["description"], "")


def main():
    # Seprating coustom arguments from normal unittest argument
    argv_tpl = (
        "--update-readme",
        "--clear-trailling-space",
    )  # Expected coustom arguments
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

    if "--update-readme" in coustom_argv:
        update_readme()
    if "--clear-trailling-space" in coustom_argv:
        clear_trailling_space()


if __name__ == "__main__":
    main()
