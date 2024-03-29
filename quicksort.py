## Divide and conquer without merging.
## Know the median value of the list. Half would be lesser than this value half would be greater than this value.
## Right half > m thus shifting here could be done inplace with O(n)
##Recursively sorting left and right values; no need of merging.
## Complexity is thus: T(n) = 2T(n/2) + n = O(nlogn)

## But how do we choose a median in an unsorted list when the goal is to sort the list? 
## Answer: Choose a pivot(typically 1st element) from the list and then proceed.
## Algorithm was invented by: C.A.R. Hoare and is one of the famous sorting algorithms.

## Worst case: a) When pivot is either maximum or minimum(One partition is empty and the other is size n-1)
## T(n) = T(n-1)+n = T(n-2) + (n-1) + n = .... = 1+2+3+...+n = O(n2)
## b) Already sorted array is worst case input.

## Average case: O(nlogn): All permutations of n values, each equally likely.
## Randomization: fixed choice of pivot could result in worst case.
## Randomization allows us to choose any random index between range(0,n) with uniform probability.

## Applications: Spreadsheets, built in default function in programming languages.

import sys
def quicksort(A:list, l:int, r:int)->list:
    """Function to sort an unsorted list using divide and conquer without merging- quick sort technique.
    """
    if r-l <=1:
        return
    yellow = l+1
    for green in range(l+1, r):
        if A[green] <= A[l]:
            A[yellow], A[green] = A[green], A[yellow]
            yellow+=1
    A[yellow-1], A[l] =  A[l], A[yellow-1] # Moving the pivot in place
    quicksort(A, l, yellow-1)
    quicksort(A,yellow, r)
    return A

if __name__ == "__main__":
    my_list = list(map(int,sys.argv[1].split('[')[1].split(']')[0].split(',')))

    print(quicksort(my_list,0,len(my_list)))