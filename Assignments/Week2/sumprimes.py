import sys

def factors(n:int)->list:
    flist=[]
    for i in range(1, n+1):
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
    return factors(i)== [1,i]

def sumprimes(l:list)->int:
    """Function that takes in a list of numbers and returns the sum of primes.
    Params:
    ---------
    l: <list> List of numbers.

    Returns:
    ---------
    <int> : sum of prime numbers"""
    sum_primes=0
    for num in l:
        if isprime(int(num)):
            sum_primes+=int(num)
    return sum_primes

if __name__ == "__main__":
    print(sumprimes(list(sys.argv[1:])))
