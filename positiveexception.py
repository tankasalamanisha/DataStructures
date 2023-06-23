def append_new_dict_element(my_dict,k_,v_):
    try:
        my_dict[k_].append(v_)
    except KeyError as ke:
        print(f'{ke}: Key not in dict... Adding a new key entry...')
        my_dict[k_] = [v_]
    
    return my_dict

if __name__ == "__main__":
    new_dict = {"manisha":[20,30], "mohan":[50,60]}
    print(append_new_dict_element(new_dict, "Anand",50))