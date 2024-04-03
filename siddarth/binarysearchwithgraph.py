import  matplotlib.pyplot as plt
def binarysearch(array,key,start,end):
    if (start<=end):
        mid=(start+end)//2
        if (array[mid]==key):
            return mid
        elif (array[mid]<key):
            return binarysearch(array,key,mid+1,end)
        elif (array[mid]>key):
            return binarysearch(array,key,start,mid-1)
        else:
            return -1
        
array=[10,20,30,40,50]
key=50
result=binarysearch(array,key,0,len(array)-1)
if (result!=-1):
    print("the is element found=",str(result))
else:
    print("the element is not found ")

x=list(range(1,1000))
plt.plot(x, [y*y for y in x])
plt.title("selection sort time complexcity O(n\u00b2)")
plt.xlabel("input")
plt.ylabel("time")
plt.show()