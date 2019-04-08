'''
@author: Kartikei Mittal
Unit tests file for current project.
https://github.com/Kartikei-12/Connect-N
'''
# Python module(s)
import unittest

# User module(s)
from default_variables import *
from connect_n.connect_n import ConnectNGame

class ConnectNTests(unittest.TestCase):
    # Tests for project Connect-N.
    
    def test_init(self):
        # Testing instantiateing module
        print('Instantiating: ')
        game = ConnectNGame()
        self.assertEqual(game.num_col, COLUMNS)
        self.assertEqual(game.num_rows, ROWS)
        self.assertEqual(game.n, N)
        del game

    def test_version(self):
        # Testing version system
        print('Version: ')
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

if __name__ == "__main__":
    print('Testing: ')
    unittest.main()
