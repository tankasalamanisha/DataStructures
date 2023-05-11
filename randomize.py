import random
import time
from quicksort import *
import sys
sys.setrecursionlimit(100000)
def randomize(l:list):
    for i in range(len(l)//2):
        j = random.randrange(0,len(l),1)
        k = random.randrange(0,len(l),1)

        l[j], l[k] = l[k], l[j]
    return l

if __name__ == "__main__":
    l= list(range(7500,0,-1))
    start_time = time.time()
    quicksort(l,0,len(l))
    without_randomization = time.time()
    print(f"Quicksort without randomization:{without_randomization-start_time}")
    start_time = time.time()
    quicksort(randomize(l),0,len(l))
    with_randomization = time.time()
    print(f"Quicksort with randomization:{with_randomization-start_time}")
    