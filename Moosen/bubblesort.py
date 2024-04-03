import matplotlib.pyplot as plt
def bubble_sort(array):
    for i in range(len(array)):
        for j in range(0,len(array)-i-1):
            temp=array[j]
            array[j]=array[j+1]
            array[j+1]=temp

array=[50,60,50,40,80]
bubble_sort(array)
print(array)


x=list(range(1,1000))
plt.plot(x,[y*y for y in x])
plt.title("bubble_sort")
plt.xlabel("input")
plt.ylabel("time")
plt.show()