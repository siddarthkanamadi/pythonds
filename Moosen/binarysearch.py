import matplotlib.pyplot as plt
import math
def binary_search(array,key,start,end):
    if start<end:
        mid=(start+end) // 2
    if array[mid]==key:
        return mid
    elif array[mid]<key:
        return binary_search(array,key,mid+1,end)
    elif array[mid]>key:
        return binary_search(array,key,start,mid-1)
    else:
        return -1
    

array = [1,2,3,4,5,6,7]
key=7
result=binary_search(array,key,0,len(array)-1)
if result != -1:
    print("ele is present" + str(result))
else:
    print("sorry ele is not present")

x=list(range(1,1000))
plt.plot(x,[math.log(y,2 )for y in x])
plt.title("binary search")
plt.xlabel("input")
plt.ylabel("time")
plt.show()