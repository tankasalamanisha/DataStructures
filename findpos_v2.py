import sys
from typing import Union, List

def findpos(l:list, v: Union[int,float])->int:
    """Function to get the first position of the value in the list.
    Params:
    _________
    l (List): list"""
    (pos, i) = (-1,0)
    for x in l:
        if x == v:   # Exit and report position of x
            pos = i 
            break
        i = i+1

    # If pos not found , pos is -1
    return pos

if __name__ == "__main__":
    print(f"{sys.argv[2]} is found at position: {findpos(list(map(Union[int,float],sys.argv[1])),map(Union[int,float],sys.argv[2]))}")

