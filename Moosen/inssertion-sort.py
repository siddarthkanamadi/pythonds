import matplotlib.pyplot as plt
def insertion_sort(array):
    for step in range(1,len(array)):
        key = array[step]
        j=step-1
        while j>=0 and key < array[j]:
            array[j+1] =array [j]
            j=j-1
        array[j+1]=key

array=[5,6,9,8,7]
insertion_sort(array)
print(array)
x=list(range(1,1000))
plt.plot(x,[y*y for y in x])
plt.title("insertion_sort")
plt.xlabel("input")
plt.ylabel("time")
plt.show()