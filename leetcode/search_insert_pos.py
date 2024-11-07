def search_insert_pos(l:list, target:int)->int:
    """Function that returns the postion of the given target in a sorted list; if the target is not part of the list, then it inserts the target at its position and returns the position of insertion"""
    if len(l) >= 1 and len(l) <= 10**4 and target >= -10**4 and target <= 10**4:
            if target in l:
                print(l.index(target))
                return l.index(target)
            else:
                l.append(target)
                l.sort()
                return l.index(target)

if __name__ == "__main__":
    my_list = [2,3,4,8]
    target = 2
    search_insert_pos(my_list, target)