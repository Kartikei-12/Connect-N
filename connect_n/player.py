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
        # Instantiate method
        self.name = name
        self.id = next(self._ids)

    def __str__(self):
        return "<class 'Player'> {} {} ".format(self.id, self.name)
