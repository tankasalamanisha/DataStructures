import sys

def insert(seq,k):
    """Function to insert the sorted element in its position."""
    pos=k
    while pos>0 and seq[pos]< seq[pos-1]:
        seq[pos],seq[pos-1] = seq[pos-1], seq[pos]
        pos-=1
    return seq

def isort(seq,k):
    """Function to sort a sequence element-wise recursively"""
    if k>1:
        isort(seq,k-1)
        insert(seq,k-1)
    return seq
def InsertionSort(seq):
    """Function to sort a list. technique: Insertion Sort ( Recursive process)"""
    return isort(seq=seq, k=len(seq))

if __name__ == "__main__":
    my_list= list(map(int,sys.argv[1].split('[')[1].split(']')[0].split(',')))
    print(f'Sorting the list {my_list} : {InsertionSort(my_list)}')