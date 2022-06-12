import sys
def gcd(m:int,n:int)-> int :
    fm = []
    for i in range(1, m+1):
        if (m%i) == 0:
            fm.append(i)
    fn = []
    for j in range(1, n+1):
        if (n%j) == 0:
            fn.append(j)
    cf = []
    for f in fm:
        if f in fn:
            cf.append(f)
    return cf[-1]

if __name__ == "__main__" :
    print(len(sys.argv))
    print(f"Greatest Common divisor of {sys.argv[1]} and {sys.argv[2]} is:{gcd(int(sys.argv[1]),int(sys.argv[2]))}")

    