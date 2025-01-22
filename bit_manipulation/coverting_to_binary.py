import sys
def convert2binary(n):
    """Function to convert decimal number to binary equivalent
    
    Time complexity: Dividing by 2, thus it log base 2(N)
    Space Complexity: Number of steps taken = number of reminders saved. Thus log base 2(N) -> same as Time Complexity"""

    result = ""
    while n>=1:
        # print(n)
        if n%2 == 1: result += "1"
        else: result += "0"
        n = n//2
    
    return result[::-1]

if __name__ == "__main__":
    n = int(sys.argv[1])
    print(n)
    print(convert2binary(n=n))