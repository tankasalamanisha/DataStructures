import sys

def gcd(m:int, n:int)->int:
    if m < n:
        (m,n) =(n,m) # Assume m>=n if not, swap : simultaneous swap.
        
    if (m%n) == 0:
        return n # if n divides n, then n will be the greatest factor of both m and n.
    else:
        return gcd(n, m%n) # recursion
if __name__ == "__main__":
        print(f"The greatest common divisor of {sys.argv[1]} and {sys.argv[2]} is {gcd(int(sys.argv[1]),int(sys.argv[2]))}")