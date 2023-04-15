import sys

def rotate(l:list)->bool:
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
    for i in range(N):
        for j in range(i):
            temp = l_rotate[i][j]
            l_rotate[i][j] = l_rotate[j][i]
            l_rotate[j][i] = temp
 
    # Second rotation
    # with respect to middle column
    for i in range(N):
        for j in range(int(N/2)):
            temp = l_rotate[i][j]
            l_rotate[i][j] = l_rotate[i][N-j-1]
            l_rotate[i][N-j-1] = temp
    
    return l_rotate

if __name__ == "__main__":
    matrix = sys.argv[1]
    matrix = [i.split('[[')[1] if '[[' in i else i.split(']]')[0] for i in matrix.split('],[')]
    matrix= [list(m.split(',')) for m in matrix]
    matrix= [list(map(int,i)) for i in matrix]
    print(rotate(matrix))