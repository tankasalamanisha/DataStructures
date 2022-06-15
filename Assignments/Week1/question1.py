import sys

def g(n:int)->int:
    s=0
    for i in range(2,n):
        if n%i ==0:
            s+=1
    return s

if __name__ == "__main__":
    print(f"Greatest divisor of {sys.argv[1]} : {g(int(sys.argv[1]))} - Greatest divisor of {sys.argv[2]}: {g(int(sys.argv[2]))} is : {g(int(sys.argv[1]))- g(int(sys.argv[2]))}") 
