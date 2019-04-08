'''
@author: Kartikei Mittal
@email: kartikeimittal@gmail.com
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
        print('Testing Instantiating: ')
        game = ConnectNGame()
        self.assertEqual(game.num_col, COLUMNS)
        self.assertEqual(game.num_rows, ROWS)
        self.assertEqual(game.n, N)
        del game

    def test_version(self):
        # Testing version system
        print('Testing Instantiating: ')
        game = ConnectNGame()
        try: # Integrating file number.
            with open(, 'r') as f:
                temp = f.read()
                f.close()
                return temp
        except FileNotFoundError:
            return ''

if __name__ == "__main__":
    unittest.main()    
