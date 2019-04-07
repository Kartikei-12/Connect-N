'''
@author: Kartikei Mittal
@email: kartikeimittal@gmail.com
__init__.py file connect_n module
Tasks:
    Increment Version Number
https://github.com/Kartikei-12/Connect-N
'''

import os
file_path = os.path.dirname(os.path.realpath(__file__)) + '/version.txt'

try:
    '''
    Version Maintainance.
    Every time anything from connect_m module is imported it's version number
    in file version.txt is incremented by one. 
    '''
    version = str(int(open(file_path, 'r').read()) + 1)
    with open(file_path, 'w')as f:
        f.write(version)
        f.close()
except FileNotFoundError or ValueError:
    '''
    version.txt missing.
    '''
    with open(file_path, 'w+') as f:
        f.write('1')
        f.close()
