import sys

def rotatelist(l:list,k:int)->list:
    """Function that rotates a list k times.
    Params:
    ---------
    l(list): list of numbers.
    k(int): Number of times the list has to be rotated.

    Returns:
    ---------
    <list>: rotated list.
    """
    if k>0:
        temp = l[:k]
        rotated_list = l[k:]
        rotated_list.extend(temp)
        return rotated_list
    else:
        return l

if __name__ == "__main__":
    print(f"Rotated list is: {rotatelist(list(map(int,sys.argv[1])),int(sys.argv[2]))}")

