import sys

def factors(n:int)->list:
    flist=[]
    for i in range(1, n+1):
        if n%i == 0:
            flist= flist+ [i]
    return flist

if __name__ == '__main__':
    print(f"Factors of {sys.argv[1]} : {factors(int(sys.argv[1]))}")
