import sys
import numpy as np

def matrixflip(l:list, flip:str)->list:
    """Function to rotate the given matrix

    Args:
        l(list): matrix to be rotated

    Returns:
        l_rotate: rotated list
    """
    flipped_matrix = l
    if flip == 'h':
        flipped_matrix=np.flip(flipped_matrix,axis=1)
    elif flip == 'v':
        flipped_matrix=np.flip(flipped_matrix,axis=0)
    
    return flipped_matrix

if __name__ == "__main__":
    matrix = sys.argv[1]
    matrix = [i.split('[[')[1] if '[[' in i else i.split(']]')[0] for i in matrix.split('],[')]
    matrix= [list(m.split(',')) for m in matrix]
    matrix= [list(map(int,i)) for i in matrix]
    print(matrixflip(matrix, sys.argv[2]))