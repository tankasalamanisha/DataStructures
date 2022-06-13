import sys
def gcd(m: int, n:int)->int:
    """
    Function definition to compute greatest common divisor of 2 numbers.
    Parameters:
    -------------
    m, n -> input from user; type: int.
    Returns:
    -------------
    cf[-1] -> greates common divisor of m and n"""
    cf=[] # initialising an empty list.
    for i in range(1,min(m,n)+1):
        if m%i == 0 and n%i ==0 :
            cf.append(i)
    return cf[-1]

if __name__ == "__main__":
    print(f"Greatest common divisor of {sys.argv[1]} and {sys.argv[2]} is: {gcd(int(sys.argv[1]), int(sys.argv[2]))}")