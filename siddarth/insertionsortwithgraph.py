import matplotlib.pyplot as plt
def insertionsort(array):
    for i in range(0,len(array)):
        key=array[i]
        j=i-1
        while j>=0 and key<array[j]:
            array[j+1]=array[j]
            j=j-1
        array[j+1]=key

array=[10,50,30,20,40]
insertionsort(array)
print(array)
x=list(range(1,1000))
plt.plot(x, [y*y for y in x])
plt.title("insertion sort time complexcity O(n\u00b2)")
plt.xlabel("input")
plt.ylabel("time")
plt.show()