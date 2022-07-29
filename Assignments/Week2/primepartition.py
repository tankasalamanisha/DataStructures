import sys

def isprime(num):
    """Function to check if a number is a prime number."""
def primes(num):
    """Function to partition a number into list of primes.
    Params:
    --------
    num (int): Input number.

    Returns:
    ---------
    <list>: List of primes"""
    primelist =set()
    for i in range(2, num+1):
        for p in range(2,i):
            if (i%p) == 0:
                break
            else:
                primelist.add(i)
    return list(primelist)

def primepartition(num:int)->bool:
    """Function to check if an input number can be partitioned into primes.

    Params:
    ---------
    num (int): Input number.

    Returns:
    ---------
    <bool> : Whether a number can be partitioned into list of primes or not.
    """

    primelist = primes(num)
    if sum(primelist) == num:
        return True
    else:
        return False

if __name__ == "__main__":
    if primepartition(int(sys.argv[1])):
        print(f"{sys.argv[1]} can be partitioned into: {primes(int(sys.argv[1]))}")
    else:
        print(f"{sys.argv[1]} cannot be partitioned into primes.{primes(int(sys.argv[1]))}")
