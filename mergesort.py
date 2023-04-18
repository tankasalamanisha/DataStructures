import sys
from merge import *

def mergesort(A,left,right):
    if right - left <=1: #Base case
        return A[left:right]
    if right - left >1:  # Recursive call
        mid = (left+right)//2

        L = mergesort(A= A, left=left, right=mid)
        R = mergesort( A=A, left=mid, right= right)

        return merge(L,R)

if __name__ == "__main__":
    my_list = list(map(int,sys.argv[1].split('[')[1].split(']')[0].split(',')))

    print(mergesort(my_list,0,len(my_list)))