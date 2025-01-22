import sys
def convert2dec(n):
    """Function to convert Binary number to Decimal equivalent
    
    Time complexity: Dividing by 2, thus it log base 2(N)
    Space Complexity: Number of steps taken = number of reminders saved. Thus log base 2(N) -> same as Time Complexity"""

    p2=1
    num = 0
    for i in range(len(n)-1,-1,-1):
        if n[i] == "1":
            num += 1*p2
        p2 = p2*2
    
    return num

if __name__ == "__main__":
    n = sys.argv[1]
    print(n)
    print(convert2dec(n=n))