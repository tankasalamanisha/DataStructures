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
        diff = abs(l[i+1]- l[i])
        diff_list.append(diff)
    #Checking for a sorted list: ascending
    is_sorted= True
    for i in range(1, len(diff_list)):
        if diff_list[i] <= diff_list[i - 1]:
            is_sorted= False
    return is_sorted

if __name__ == "__main__":
    print(expanding(list(map(int,sys.argv[1]))))