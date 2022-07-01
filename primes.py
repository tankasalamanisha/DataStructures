import sys
from factors1 import factors  # importing the function factors from the code in the file factors1.py

def isprime(i:int)->bool:
    """Function to return if the number is prime or not.
    Params:
    _________
    i : <int> Input number to be checked for prime.
    
    Returns:
    <bool> : True if the number is prime, False otherwise."""
    return factors(i)== [1,i]

def primesupto(n:int)->list:
    """Function to return prime numbers upto specified target number.
    Params:
    _________
    n: <int> Input target upto which prime numbers need to be generated.

    Returns:
    _________
    primelist: <list> List of prime numbers upto the target n.
    """
    primelist = []
    for i in range(1,n+1):
        if isprime(i):
            primelist = primelist +[i]
    return primelist

if __name__ == "__main__":
    print(f'Primes upto {sys.argv[1]} == {primesupto(int(sys.argv[1]))}')
