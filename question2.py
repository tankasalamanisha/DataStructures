import sys

def h(x:int)->int:
    (d,n) = (1,0)
    while d<=x:
        (d,n) = (d*3,n+1)
    return n

if __name__ == "__main__":
    print(f' h({sys.argv[1]}) = {h(int(sys.argv[1]))}')  
