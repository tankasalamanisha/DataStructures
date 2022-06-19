import sys

def h(x:int)->int:
    (m,a) =(1,0)
    while m <= x:
        (m,a) = (m*2,a+1)
    return a

if __name__ == "__main__":
    print(f"h({sys.argv[1]})={h(int(sys.argv[1]))}")
