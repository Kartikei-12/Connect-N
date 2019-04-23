"""
@author: Kartikei Mittal

player.py file

Contains player module.

https://github.com/Kartikei-12/Connect-N
"""

# Python module(s)
from itertools import count


class Player:
    """Player class
    
    Args:
        name (str): Name of the player
    """

    _ids = count(1)

    def __init__(self, name=""):
        """Instantiate method"""
        self.name = name
        self.id = next(self._ids)

    def get_move(self):
        """Simple method to ask for player move"""
        msg = "Player {0} make your move: ".format(self.name)
        try:
            col = int(input(msg)) - 1
        except ValueError as e:
            print(e, "Aborting current turn, moving ahead.")
            return -1  # Signifies invalid type of input
        else:
            return col

    def __str__(self):
        """String representation of class object"""
        return "<class 'Player'> {} {} ".format(self.id, self.name)
