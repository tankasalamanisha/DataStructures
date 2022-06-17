import sys

def divides(m:int,n:int)->bool:
    """Function that returns True if m divides n; and False if not."""
    if n%m == 0:
        return True
    return False
def even(n:int)->bool:
    """Function that returns True if a number passed is an Even number"""
    return divides(2,n)

def odd(n:int)->bool:
    """Function that returns True if a number passed is an Odd number"""
    return not divides(2,n)

if __name__ == "__main__":
    n = int(sys.argv[1])
    if even(n):
        print(f'{n} is an Even number')
    elif odd(n):
        print(f'{n} is an Odd number')
    else:
        print(f'{n} is niether even nor odd')
    
