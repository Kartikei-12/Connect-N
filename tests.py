'''
@author: Kartikei Mittal
Unit tests file for current project.
https://github.com/Kartikei-12/Connect-N
'''
# Python module(s)
import time
import unittest

# User module(s)
from default_variables import *
from connect_n.player import Player
from connect_n.connect_n import ConnectNGame

class ConnectNTests(unittest.TestCase):
    # Tests for project Connect-N.
    
    def test_init(self):
        # Testing instantiateing module
        print('\nInstantiating: ')
        game = ConnectNGame()
        self.assertEqual(game.num_col, COLUMNS)
        self.assertEqual(game.num_rows, ROWS)
        self.assertEqual(game.n, N)
        del game

    def test_version(self):
        # Testing version system
        print('\nVersion: ')
        game = ConnectNGame()
        temp = '*'
        try:
            with open('connect_n/version.txt', 'r') as f:
                temp = f.read()
                f.close()
        except FileNotFoundError:
            pass
        self.assertEqual(temp, game.__version__[5:])
        del game
        del temp

    def test_winning_move(self):
        # Testing Winning move
        print('\nWinning Move: ')
        game = ConnectNGame(3, 3, 3)
        
        game.board = [[1.0, 1.0, 1.0],
                      [0.0, 0.0, 0.0],
                      [0.0, 0.0, 0.0]]
        self.assertTrue(game.is_winning_move(0, 2))
        game.board = [[1.0, 0.0, 0.0],
                      [1.0, 0.0, 0.0],
                      [1.0, 0.0, 0.0]]
        self.assertTrue(game.is_winning_move(2, 0))
        game.board = [[1.0, 2.0, 2.0],
                      [0.0, 1.0, 2.0],
                      [0.0, 0.0, 1.0]]
        self.assertTrue(game.is_winning_move(1, 1))
        del game

    def test_add_player(self):
        # Testing add player method
        print('\nAdd player: ')
        game = ConnectNGame()
        p = Player('A')
        with self.assertRaises(ValueError):
            game.add_player(p)
            game.add_player(p)
        del game

if __name__ == "__main__":
    print('Testing: ')
    unittest.main()
