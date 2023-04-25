import sys

def transpose(l:list)->list:
    """Function to get a transpose the given matrix

    Args:
        l(list): matrix to be transposed

    Returns:
        l_rotate: transposed matrix
    """

    temp=[[l[j][i] for j in range(len(l))] for i in range(len(l[0]))]

    return temp

if __name__ == "__main__":
    matrix = sys.argv[1]
    matrix = [i.split('[[')[1] if '[[' in i else i.split(']]')[0] for i in matrix.split('],[')]
    matrix= [list(m.split(',')) for m in matrix]
    matrix= [list(map(int,i)) for i in matrix]
    print(transpose(matrix))