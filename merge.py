import sys

def merge(A,B):
    """Function to merge two sorted lits
    Args:
    A(list): Input list 1
    B(list):Input list 2
    Returns:
    list: merged sorted list."""
    C,m,n = [],len(A), len(B)
    i,j = 0,0

    while i+j < m+n:

        if i==m:
            C.append(B[j])
            j+=1
        elif j == n:
            C.append(A[i])
            i+=1
        elif A[i] <= B[j]:
            C.append(A[i])
            i+=1
        elif A[i] >= B[j]:
            C.append(B[j])
            j+=1
    return C

if __name__ == "__main__":
    list_1 = list(map(int,sys.argv[1].split('[')[1].split(']')[0].split(',')))
    list_2 = list(map(int,sys.argv[2].split('[')[1].split(']')[0].split(',')))

    d= merge(list_1, list_2)
    print(d)
