'''
@author: Kartikei Mittal
@email: kartikeimittal@gmail.com
main.py file for demostrating use of connect_n module.
https://github.com/Kartikei-12/Connect-N
'''

__author__ = 'Kartikei Mittal'
__email__ = 'kartikeimittal@gmail.com'

# User module(s)
from connect_n.player import Player
from connect_n.connect_n import ConnectNGame

print('Hello World!!\n-------------------------------------------------------------------')

if __name__ == "__main__":
    # Main program block of the project.
    game = ConnectNGame()
    print(game)
    print(game.__version__)
    game.add_player(Player('A'))
    game.add_player(Player('B'))
    game.play_game_graphic()
    # game.play_game()

print('---------------------------------------------------------------------\nBye World!!')

