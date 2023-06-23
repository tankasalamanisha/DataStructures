import numpy as np
import sys
import re

def rainaverage(l:list)->list:
    """Function to compute rain average of the entries for cities
    
    Args:
    ---------------------
    l: list of tuple entries for (city, rainfall_record).

    Returns:
    ---------------------
    list: list of tuples containing (city, rainfall_average)
    """
    rainfall_dict={}
    for (city,rainfall) in l:
        try:
            rainfall_dict[city].append(rainfall)
        except KeyError as ke:
            print(f'{ke}: City entry not present... Adding new city..')
            rainfall_dict[city] = [rainfall]
    
    rainfall_dict_2 ={}
    for city, rainfall in rainfall_dict.items():
        rainfall_dict_2[city] = np.mean(rainfall)
    #dict(sorted(words.items(), key=lambda x: x[1]))

    rainfall_dict_2 = dict(sorted(rainfall_dict_2.items(), key=lambda x:x[0]))
    
    rainfall_tuple = list(rainfall_dict_2.items())
    
    return rainfall_tuple

if __name__ == "__main__":
    mylist = sys.argv[1].split('),(')
    mylist = [[i.split(',')[0], i.split(',')[1]] for i in mylist]
    mylist[0][0]=mylist[0][0].split('[(')[1]
    mylist[-1][-1]=mylist[-1][-1].split(')]')[0]
    mylist = [tuple([int(i[0]), int(i[1])]) if i[0].isdigit() else tuple([i[0], int(i[1])]) for i in mylist]
    print(rainaverage(mylist))