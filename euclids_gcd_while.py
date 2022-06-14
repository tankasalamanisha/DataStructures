import sys

def gcd(m:int , n:int)->int:
    """
    Function definition to compute greatest common divisor of 2 numbers.
    Parameters:
    -------------
    m, n -> input from user; type: int.
    Returns:
    -------------
    n -> most recent greates common divisor of m and n"""
    if  m<n : #Assume  m>=n
        (m,n) = (n,m)  #  simultaneous assignment
    
    while (m%n) !=0:
        diff = m-n  #diff >n ? Possible
        (m,n) = (max(n,diff), min(n,diff))
    return n
    
    

if __name__ == "__main__":
    print(f"Greatest common divisor of {sys.argv[1]} and {sys.argv[2]} is: {gcd(int(sys.argv[1]), int(sys.argv[2]))}")