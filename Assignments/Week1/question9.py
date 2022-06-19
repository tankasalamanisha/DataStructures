import sys

def f(n:int)->int:
    s=0
    for i in range(2,n):
        if n%i == 0 and i%2 ==1:
            s=s+1
    return s

if __name__ == "__main__":
    print(f"f({sys.argv[1]})={f(int(sys.argv[1]))}")
