import sys

def leftrotate(l:list)->bool:
    """Function to rotate the given matrix

    Args:
        l(list): matrix to be rotated

    Returns:
        l_rotate: rotated list
    """
    row, col = len(l[0]) , len(l[1])

    
    l_rotate = l
    N= col
    # with respect to main diagonal
    anti_clock_rotated_mat = list(zip(*l))[::-1]
    
    anti_clock_rotated_mat=[list(l_) for l_ in anti_clock_rotated_mat]
    
    return anti_clock_rotated_mat

if __name__ == "__main__":
    matrix = sys.argv[1]
    matrix = [i.split('[[')[1] if '[[' in i else i.split(']]')[0] for i in matrix.split('],[')]
    matrix= [list(m.split(',')) for m in matrix]
    matrix= [list(map(int,i)) for i in matrix]
    print(leftrotate(matrix))