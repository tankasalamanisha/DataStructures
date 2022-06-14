import sys

def gcd(m:int , n:int)->int:
    """
    Function definition to compute greatest common divisor of 2 numbers.
    Parameters:
    -------------
    m, n -> input from user; type: int.
    Returns:
    -------------
    gcd computed recursively using euclids algorithm"""
   #Assume  m>=n
    if  m<n : 
        (m,n) = (n,m)  #  simultaneous assignment
    if (m%n) ==0:
        return n
    diff = m-n  #diff >n ? Possible
    return gcd(max(n,diff), min(n,diff))

if __name__ == "__main__":
    print(f"Greatest common divisor of {sys.argv[1]} and {sys.argv[2]} is: {gcd(int(sys.argv[1]), int(sys.argv[2]))}")