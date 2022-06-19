import sys

def f(x:int)->int:
    d=0
    while x>=1:
        (x,d)=(x/5,d+1)
    return d

if __name__ == "__main__":
    print(f"f({sys.argv[1]})= {f(int(sys.argv[1]))}")
