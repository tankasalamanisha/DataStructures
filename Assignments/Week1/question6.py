import sys

def g(n:int)->int:
    s=0
    for i in range(1,n+1):
        if n%i ==0:
            s=s+1
    return s

if __name__ == "__main__":
    print(f"No. of divisors of{sys.argv[1]}- No. of divisors of {sys.argv[2]} ={g(int(sys.argv[1]))-g(int(sys.argv[2]))}")
