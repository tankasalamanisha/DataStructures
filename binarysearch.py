import sys

def bsearch(seq:list, v:int, l:int, r:int)->bool:
    """Function that searches for a value in a sorted array/list
    Params:
    ----------
    seq(list): sorted array/list.
    v(int): value to be searched.
    l(int): left-most position.
    r(int): right-most position.
    
    Returns:
    ---------
    bool: True if the value is found, Flase otherwise
    """
    if (r-l) == 0:
        return False
    mid = (l+r)//2  # integer division
    if v==seq[mid]:
        return True
    elif v<seq[mid]:
        return bsearch(seq,v,l,mid)
    else:
        return bsearch(seq,v,mid,r)

if __name__ == "__main__":
    flag = bsearch(list(map(int,sys.argv[1])), int(sys.argv[2]), 0, len(sys.argv[1]))

    if flag:
        print(f"Value: {sys.argv[2]} is present in the list")
    else:
        print("Not found")
