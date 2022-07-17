import sys
from typing import Union
def findpos(l : list,v : Union[int,float])->int:
    """
    Function that returns the index of first occurance of a value in the list.
    Params:
    --------
    l (list): List of numbers.
    v (int/ float): value to be fetched in the list l.
    
    Returns:
    ________
    <int>: Position/index of first occurance of the element."""
    (found,i) = (False,0)

    while i< len(l):
        if not found and l[i] == v:
            (found,pos) = (True,i)

        i+=1
    if not found:
        pos = -1
    return pos

if __name__ == "__main__":
    print(f"Position of {sys.argv[2]} in list: {sys.argv[1]}: {findpos(list(map(float,sys.argv[1])),float(sys.argv[2]))}")
