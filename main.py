"""@author: Kartikei Mittal

@email: kartikeimittal@gmail.com

main.py file for demostrating use of connect_n module.

https://github.com/Kartikei-12/Connect-N"""

__author__ = "Kartikei Mittal"
__email__ = "kartikeimittal@gmail.com"

# User module(s)
from connect_n.player import Player
from connect_n.connect_n import ConnectNGame


if __name__ == "__main__":
    # game = ConnectNGame(graphic=True, ai=True, record=False)
    # game.add_player(Player("Human Player"))
    # game.play()
    from connect_n.ai_rnn.generate_data import GenerateData

    gd = GenerateData(game_runs=1)
    print(gd)
    b = gd.generate_save(want_return=True)
    a = gd.load()
    import numpy as np

    print("A\n\n", np.flip(a[0][-1], 0))
    print(a.shape)
    print(b.shape)
