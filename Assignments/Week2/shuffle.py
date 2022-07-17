import sys

def shuffle(l1:list, l2:list)->list:
    """
    Function to shuffle two lists in the order of indexes.
    Params:
    --------
    l1, l2 (List) : Two input lists to be shuffled.
    
    Returns:
    <List> : Shuffled list; if the length of teo lists are different, the remaining elements of longer list are appended at the end of shuffled output.
    """
    shuffled_list = []
    if len(l1) == len(l2):
        for i in range(len(l1)):
            shuffled_list.extend([l1[i],l2[i]])
        return shuffled_list
    elif len(l1) > len(l2):
        for i in range(len(l1)):
            try:
                shuffled_list.extend([l1[i],l2[i]])
            except:
                shuffled_list.append(l1[i])
        return shuffled_list
    else:
        for i in range(len(l2)):
            try:
                shuffled_list.extend([l1[i],l2[i]])
            except:
                shuffled_list.append(l2[i])
        return shuffled_list

if __name__ == "__main__":
    print(f"Shuffled_list: {shuffle(list(map(int,sys.argv[1])),list(map(int,sys.argv[2])))}")
