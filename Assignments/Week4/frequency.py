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
    print(freq_dict)
    freq_dict_rev ={k:[] for k in freq_dict.values()}
    for k_,v_ in freq_dict.items():
        if not freq_dict_rev[v_]:
            freq_dict_rev[v_] = [int(k_)]
        else:
            freq_dict_rev[v_].append(int(k_))
    print(freq_dict_rev)
    
    sorted_list = sorted(freq_dict_rev, key=lambda k: freq_dict_rev[k])
    print(sorted_list)
    min_value = sorted(freq_dict_rev[sorted_list[0]])
    max_value = sorted(freq_dict_rev[sorted_list[-1]])
    
    minmax = (min_value,max_value)
    return minmax

if __name__ == "__main__":

    my_list=sys.argv[1].split('[')[1].split(']')[0].split(',')
    print(frequency(my_list))
