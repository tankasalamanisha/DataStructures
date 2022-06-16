import sys

def g(m,n):
    res = 0
    while m >= n:
        (res,m) = (res+1,m/n)
    return(res)

if __name__ == "__main__" :
    print(f"For  g(m ={sys.argv[1]},n={sys.argv[2]}) : {g(int(sys.argv[1]),int(sys.argv[2]))}") 
