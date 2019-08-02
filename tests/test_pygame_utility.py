"""PyGame/GUI Tests"""

# Python module(s)
import unittest

# User module(s)
from env import UNIT_SCORE

# Project module(s)
from connect_n.ai import AI
from connect_n.connect_n import ConnectNGame


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


def main():
    """Test Runner"""
    unittest.main(verbosity=3)


if __name__ == "__main__":
    main()
