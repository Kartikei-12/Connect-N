"""@author: Kartikei Mittal

__init__.py file connect_n module"""

__author__ = "Kartikei Mittal"
__version__ = "0.1d"
__email__ = "kartikeimittal@gmail.com"

# Python module(s)
import os

# User module(s)
from .connect_n import ConnectNGame
from .player import Player
from .ai_nn import Preprocess, GenerateData
from .env import *

FILE_PATH = os.path.dirname(os.path.realpath(__file__)) + "/version.txt"

try:
    version = str(int(open(FILE_PATH, "r").read()) + 1)
    open(FILE_PATH, "w").write(version)
    del version
except (FileNotFoundError, ValueError):  # version.txt missing
    with open(FILE_PATH, "w+") as f:
        f.write("1")
        f.close()
