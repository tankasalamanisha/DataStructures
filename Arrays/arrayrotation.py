def rotated(array,n,d):
    for i in range(d):
        temp = []
        temp.append(array.pop(i))
    return temp.append(array)


n= int(input("Enter the size of array: "))
array=[]
for _ in range(n):
    ele=int(input())
    array.append(ele)
d= int(input("Enter the rotation dimension: "))
rotarray = rotated(array,n,d)
print(f"Rotated Array: {rotarray}.")