"""@author: Kartikei Mittal

@email: kartikeimittal@gmail.com

main.py file for demostrating use of connect_n module.

https://github.com/Kartikei-12/Connect-N"""

# User module(s)
from connect_n import Player
from connect_n import ConnectNGame

if __name__ == "__main__":
    game = ConnectNGame(graphic=True, ai=True, record=False)
    game.add_player(Player("Human Player"))
    game.play()
    # from connect_n.ai_nn.generate_data import GenerateData
    # gd = GenerateData(game_runs=750, file_name='dl_train_dataset_final')
    # gd.generate_save(want_return=False)
    # a = gd.load()
    # print(a.shape)
