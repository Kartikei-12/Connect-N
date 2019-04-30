"""@author: Kartikei Mittal

__init__.py file connect_n module

Tasks:
*  Increment Version Number

https://github.com/Kartikei-12/Connect-N"""

import os

FILE_PATH = os.path.dirname(os.path.realpath(__file__)) + "/version.txt"

try:
    version = str(int(open(FILE_PATH, "r").read()) + 1)
    open(FILE_PATH, "w").write(version)
except (FileNotFoundError, ValueError):
    # version.txt missing.
    with open(FILE_PATH, "w+") as f:
        f.write("1")
        f.close()
