import matplotlib.pyplot as plt
import math
def quicksort(array):
    if len(array) <1:
        return array
    else:
        pivot = array[0]
        left=[x for x in array[1:]if x < pivot]
        right=[x for x in array[1:]if x > pivot]
        return quicksort(left)+[pivot]+quicksort(right)

array=[5,4,8,7,9]
quicksort(array)
print(array)


x=list(range(1,1000))
plt.plot(x,[y*y for y in x])
plt.title("quicksort")
plt.xlabel("input")
plt.ylabel("time")
plt.show()

