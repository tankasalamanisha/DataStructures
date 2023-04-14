import sys

def expanding(l:list)->bool:
    """Function to check if the given list is expanding.

    Args:
        l(list): input list containing numbers

    Returns:
        bool: whether the given list is expanding or not.
    """
    diff_list=[]
    for i in range(len(l)-1):
        diff = l[i+1]- l[i]
        diff_list.append(diff)
    #Checking for a sorted list: ascending
    is_sorted = all(a <= b for a, b in zip(diff_list, diff_list[1:]))

    return is_sorted

if __name__ == "__main__":
    print(expanding(list(map(int,sys.argv[1]))))