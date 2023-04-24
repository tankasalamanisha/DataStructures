import sys

def remdup(l:list)->list:
    """Function that removes duplicates and returns only last occurrences of elements in the list.
    Args:
        l(list): input list containing numbers

    Returns:
        list: list of de-duplicated elements.
    """
    de_duplicated_list= []
    for ele in l:
        if ele not in de_duplicated_list:
            de_duplicated_list.append(ele)
        else:
            de_duplicated_list.remove(ele)
            de_duplicated_list.append(ele)

    return de_duplicated_list

if __name__ == "__main__":
    my_list=sys.argv[1].split('[')[1].split(']')[0].split(',')
    print(remdup(list(map(int,my_list))))