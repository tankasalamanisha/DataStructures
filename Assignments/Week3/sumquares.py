import sys

def sumsquare(l:list)->list:
    """Function that returns square sums of [odd , even] in the list
    Args:
        l(list): input list containing numbers

    Returns:
        list: square sums of [odd , even] in the list
    """
    square_sum_list= []
    odd_sum = 0
    even_sum=0
    for ele in l:
        if ele%2 == 0:
            even_sum+= ele**2
        else:
            odd_sum+= ele**2
    square_sum_list.append(odd_sum)
    square_sum_list.append(even_sum)

    return square_sum_list

if __name__ == "__main__":
    my_list=sys.argv[1].split('[')[1].split(']')[0].split(',')
    print(sumsquare(list(map(int,my_list))))