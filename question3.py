import sys

def f(m:int)->int:
    if m==0:
        return 0
    else:
        return m+f(m-1)

if __name__ == "__main__":
    print(f"Value of f({sys.argv[1]}) = {f(int(sys.argv[1]))}")
