import sys

def splitsum(l:list)->list:
    """Function that removes duplicates and returns only last occurrences of elements in the list.
    Args:
        l(list): input list containing numbers

    Returns:
        list: list of de-duplicated elements.
    """
    split_sum_list= []
    pos_sum = 0
    neg_sum=0
    for ele in l:
        if ele>0:
            pos_sum+= ele**2
        else:
            neg_sum+= ele**3
    split_sum_list.append(pos_sum)
    split_sum_list.append(neg_sum)

    return split_sum_list

if __name__ == "__main__":
    my_list=sys.argv[1].split('[')[1].split(']')[0].split(',')
    print(splitsum(list(map(int,my_list))))