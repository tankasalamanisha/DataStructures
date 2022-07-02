import sys
def interverse(n:int)->int:
    """Function to return a reversed integer.
    Params:
    _________
    n : <int> Input integer.

    Returns:
    __________
    <int> : Reversed integer"""

    rev = 0
    while n>0:
        rev*=10
        digit = n%10
        rev+=digit
        n=n//10
    return rev

if __name__ == "__main__":
    if len(sys.argv) <=1 :
        print("Please enter an integer to be reversed. Format of execution: python interverse.py <integer>")
    else:
        print(f'Reversed integer of {sys.argv[1]}: {interverse(int(sys.argv[1]))}')
