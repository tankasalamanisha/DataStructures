import sys

def matrixflip(l:list, flip:str)->list:
    """Function to rotate the given matrix

    Args:
        l(list): matrix to be rotated

    Returns:
        l_rotate: rotated list
    """
    temp=[]

    for i in range(len(l)):
        temp=temp+[l[i][:]]

    if flip=='h':
      for i in range(0,len(temp),1):
              temp[i].reverse()
    elif flip=='v':
        temp.reverse()
    
    flipped_matrix = temp

    return flipped_matrix

if __name__ == "__main__":
    matrix = sys.argv[1]
    matrix = [i.split('[[')[1] if '[[' in i else i.split(']]')[0] for i in matrix.split('],[')]
    matrix= [list(m.split(',')) for m in matrix]
    matrix= [list(map(int,i)) for i in matrix]
    print(matrixflip(matrix, sys.argv[2]))