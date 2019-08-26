"""@author: Kartikei Mittal

@email: kartikeimittal@gmail.com

main.py file for demostrating use of connect_n module.

https://github.com/Kartikei-12/Connect-N"""

# User module(s)
from connect_n import Player, ConnectNGame

if __name__ == "__main__":
    game = ConnectNGame(graphic=True, ai=True, record=False)
    game.add_player(Player("Human Player"))
    game.play()
