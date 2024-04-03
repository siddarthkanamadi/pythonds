import matplotlib.pyplot as plt
def quicksort(array):
    if len(array)<=1:
        return array
    else:
        pivot = array[0]
        left=[x for x in array[1:]if x<pivot]
        right=[x for x in array[1:]if x>=pivot]
        return quicksort(left)+[pivot]+quicksort(right)

array=[10,30,20,40]
sortedarray=quicksort(array)
print(sortedarray)
x=list(range(1,1000))
plt.plot(x, [y*y for y in x])
plt.title("selection sort time complexcity O(n\u00b2)")
plt.xlabel("input")
plt.ylabel("time")
plt.show()
