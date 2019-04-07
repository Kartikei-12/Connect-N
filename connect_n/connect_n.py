'''
@author: Kartikei Mittal
@email: kartikeimittal@gmail.com
connect_n.py file
Contains main module of this repositry.
https://github.com/Kartikei-12/Connect-N
'''

__author__ = 'Kartikei Mittal'
__email__ = 'kartikeimittal@gmail.com'

class Connect_N_game:
    '''
    Main module class used Connect-N game.
    https://github.com/Kartikei-12/Connect-N
    '''
    
    __version__ = '0.1d.'

    def __init__(self, num_rows = 6, num_columns = 7, n = 4):
        '''
        '''        
        try:
            with open('version.txt', 'r') as f: self.__version__ += f.read()
        except FileNotFoundError:
            pass

        self.NUM_ROWS = num_rows
        self.NUM_COLUMNS = num_columns
        self.N = n

    def test(self):
        print(self.__version__)

    def __repr__(self):
        '''
        Representation format:
            <class 'CLASS NAME', NUMBER_OF_ROWS NUMBER_OF_COLUMNS CONNECT_LENGTH>
        '''
        return "<class '{0}', {1} {2} {3} >"\
            .format(
                self.__class__.__name__,
                self.NUM_ROWS,
                self.NUM_COLUMNS,
                self.N
            )
