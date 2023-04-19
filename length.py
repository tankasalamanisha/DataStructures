import sys

def length(l:list)->int:
    """Function to compute length of a list recursively.
    Args:
    l(list): input list.
    
    Returns:
    int: length of the list."""
    if l == []:
        return 0
    else:
        return 1+ length(l[1:])

if __name__ == "__main__":
    my_list= list(map(int,sys.argv[1].split('[')[1].split(']')[0].split(',')))
    print(f'Lenth of the list {my_list} is: {length(my_list)}')