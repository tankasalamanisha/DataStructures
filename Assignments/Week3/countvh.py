import sys

def counthv(l:list)->list:
    """Function to return valleys and hills in a list
    Args:
        l(list): input list containing numbers

    Returns:
        list: list of valleys and hill elements.
    """
    vh_list=[]
    for i in range(1,len(l)-2):
        if l[i] == max(l):
            continue
        elif l[i]> l[i-1] and l[i]> l[i+1] and l[i-1]==l[i+1]:
            vh_list.append(l[i])
        elif l[i]< l[i-1] and l[i]< l[i+1] and l[i-1]==l[i+1]:
            vh_list.append(l[i])
    if len(vh_list) == 0 and l[0]>l[1]:
        vh_list= [0,1]
    elif len(vh_list) == 0 and l[0]<l[1]:
        vh_list= [1,0]
    return vh_list

if __name__ == "__main__":
    my_list=sys.argv[1].split('[')[1].split(']')[0].split(',')
    print(counthv(list(map(int,my_list))))