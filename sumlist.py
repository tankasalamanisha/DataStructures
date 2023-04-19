import sys

def sumlist(l:list)->int:
    """Function to compute sum of a list recursively/inductively.
    Args:
    l(list): input list.
    
    Returns:
    int: length of the list."""
    if l == []: # Base case
        return 0
    else:
        return l[0]+ sumlist(l[1:]) # Recursive case

if __name__ == "__main__":
    my_list= list(map(int,sys.argv[1].split('[')[1].split(']')[0].split(',')))
    print(f'Sum of the list {my_list} is: {sumlist(my_list)}')