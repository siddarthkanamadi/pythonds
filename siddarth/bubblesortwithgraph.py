import  matplotlib.pyplot as plt
def bubblesort(array):
    for i in range(len(array)):
        for j in range(0,len(array)-i-1):
            if array[j]>array[j+1]:
                temp=array[j]
                array[j]=array[j+1]
                array[j+1]=temp

array=[10,50,40,30,20]
bubblesort(array)
print(array)
x=list(range(1,1000))
plt.plot(x, [y*y for y in x])
plt.title("selection sort time complexcity O(n\u00b2)")
plt.xlabel("input")
plt.ylabel("time")
plt.show()