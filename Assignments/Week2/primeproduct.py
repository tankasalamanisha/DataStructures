import sys


def factors(n:int)->list:
    flist=[]
    for i in range(1, n):
        if n%i == 0:
            flist= flist+ [i]
    return flist

def isprime(i:int)->bool:
    """Function to return if the number is prime or not.
    Params:
    _________
    i : <int> Input number to be checked for prime.
    
    Returns:
    <bool> : True if the number is prime, False otherwise."""
    return factors(i)== [1,i] or factors(i)== [1] or factors(i)== []

def primeproduct(n:int)->bool:
    """Function to check if the input number is a product of primes.

    Args:
        n (int): Input number.

    Returns:
        bool: True if the number is prime product; False otherwise.
    """
    factor = factors(n)
    truth_value = []
    for f in factor:
        if not isprime(f):
            truth_value.append(False)
        else:
            truth_value.append(True)
    return all(truth_value)

if __name__ == "__main__":
    print(primeproduct(int(sys.argv[1])))
