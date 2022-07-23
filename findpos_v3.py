import sys

def findpos(l,v):
    """Function to find the position of the value in the list"""
    pos = -1
    for i in range(len(l)):
        if l[i] == v: #Exit and report position.
            pos=i
            break

    #If pos not found , return -1
    return pos

if __name__ == "__main__":
    print(f"Position of {sys.argv[2]} in the list is:{findpos(list(map(int,sys.argv[1])),int(sys.argv[2]))}")
