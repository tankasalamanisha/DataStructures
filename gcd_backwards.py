import sys

def gcd(m:int , n:int)->int:
    """
    Function definition to compute greatest common divisor of 2 numbers.
    Parameters:
    -------------
    m, n -> input from user; type: int.
    Returns:
    -------------
    mrcf -> most recent greates common divisor of m and n"""
    mrcf=1
    i= min(m,n)
    while i>0:
        if m%i==0 and n%i==0 :
            return i
        else:
            i=i-1
if __name__ == "__main__":
    print(f"Greatest common divisor of {sys.argv[1]} and {sys.argv[2]} is: {gcd(int(sys.argv[1]), int(sys.argv[2]))}")