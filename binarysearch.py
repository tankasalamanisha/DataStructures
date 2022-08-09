import sys

def binarysearch(seq:list, v:int)->bool:
    """Function to search an element in an unsorted list/array.
    Params:
    ---------
    seq : list of unsorted values.
    v (int): value to be searched.
    Returns:
    ---------
    bool : whether the value is present or not in the list.
    """
    for x in seq:
        if x==v:
            return True
    return False
if __name__ == "__main__":
    if binarysearch(seq = list(map(int,sys.argv[1])),v = int(sys.argv[2])):
        print(f"The value {sys.argv[2]} is found in the list")
    else:
        print("Not found")

