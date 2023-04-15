import sys

def accordian(l:list)->bool:
    """Function to check if the given list is accordion list.

    Args:
        l(list): input list containing numbers

    Returns:
        bool: whether the given list is accordion or not
    """
    diff_list=[]
    for i in range(len(l)-1):
        diff = l[i+1]- l[i]
        diff_list.append(diff)
    #Returning a list of True False for increrase(True) and decrease(False)

    true_false_list = [a <= b for a, b in zip(diff_list, diff_list[1:])]

    is_accordion = (all(x!= y for x, y in zip(true_false_list, true_false_list[1:])))
    
    if len(true_false_list)<=2:
        is_accordion = False

    return is_accordion

if __name__ == "__main__":
    print(accordian(list(map(int,sys.argv[1]))))