import sys

def update(l,i,v):
    if i >= 0 and i <= len(l):
        l[i] = v
        return True
    else:
        v = v+1
        return False
if __name__ == '__main__':
    if len(sys.argv)<=1:
        print(f'Please run the file with the arguments: python3 functions.py [list of numbers], position, update_value')
    else:
        print(f'The list {sys.argv[1]} after update is: {update(list(sys.argv[1]), int(sys.argv[2]),(int(sys.argv[3])))}: {sys.argv[1]}')
