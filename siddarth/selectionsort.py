import matplotlib.pyplot as plt
def selectionsort(array):
    for  i in range (0,len(array)):
        mini=i
        for j in range(i+1,len(array)):
            if array[j]<array[mini]:
                mini=j
                array[i],array[mini]=array[mini],array[i]

array=[20,10,30,40,60,50]
selectionsort(array)
print(array)
x=list(range(1,1000))
plt.plot(x, [y*y for y in x])
plt.title("selection sort time complexcity O(n\u00b2)")
plt.xlabel("input")
plt.ylabel("time")
plt.show()