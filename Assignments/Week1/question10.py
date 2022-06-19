import sys

def h(n:int)->int:
    s=0
    for i in range(1,n+1):
        if n%i >0:
            s=s+1
    return s

if __name__ == "__main__":
    print(f'h({sys.argv[1]}) - h({sys.argv[2]}) = {h(int(sys.argv[1]))- h(int(sys.argv[2]))}')
