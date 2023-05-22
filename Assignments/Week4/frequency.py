import sys
import numpy as np

def frequency(l:list)->tuple:
    """Function that returns the tuple of max frequency number and min frequency number in a given list.
    Args:
    -----------------------
    l: list of numbers.
    Returns:
    -----------------------
    tuple: tuple containing the number that's least number of times repeated and the number that's max number of times repeated.
    """
    freq_dict={}
    for ele in l:
        if ele in freq_dict:
            freq_dict[ele]+=1
        else:
            freq_dict[ele] = 1
    sorted_list = sorted(freq_dict, key=lambda k: freq_dict[k])
    print(sorted_list)
    min_value = sorted_list[0]
    max_value = sorted_list[0]
    for v_ in sorted_list:
        if min_value > v_:
            min_value = v_
        if max_value < v_:
            max_value = v_
    
    minmax = ([int(min_value)],[int(max_value)])
    return minmax

if __name__ == "__main__":

    my_list=sys.argv[1].split('[')[1].split(']')[0].split(',')
    print(frequency(my_list))
