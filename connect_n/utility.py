'''
@author: Kartikei Mittal
Utility mathods
'''

def getVersion(file):
    '''Method
    Args:
        file (str): File path(usually to the file version.txt)
    Returns:
        Version after reading from given file.
    '''
    try: # Integrating file number.
        with open(file, 'r') as f:
            temp = f.read()
            f.close()
            return temp
    except FileNotFoundError:
        return ''
