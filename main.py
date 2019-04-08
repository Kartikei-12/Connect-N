'''
@author: Kartikei Mittal
@email: kartikeimittal@gmail.com
main.py file for demostrating use of connect_n module.
https://github.com/Kartikei-12/Connect-N
'''

__author__ = 'Kartikei Mittal'
__email__ = 'kartikeimittal@gmail.com'

from connect_n.connect_n import ConnectNGame

print('Hello World!!')

if __name__ == "__main__":
    # Main program block of the project.
    game = ConnectNGame()
    print(game)
    print(game.__version__)
    game.print_board()

print('Bye World!!')

