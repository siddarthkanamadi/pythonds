import matplotlib.pyplot as plt
def selection_sort(array,size):
    for i in range(size):
        min_idx=i
        for j in range(i+1,size):
            if array[j]<array[min_idx]:
                min_idx=j
        (array[i],array[min_idx])=(array[min_idx],array[i])


array=[9,8,7,6,3,5,4,2,1]
size=len(array)
selection_sort(array,size)
print("\n Array in ascending order")
print(array)
x=list(range(1,10000))
plt.plot(x,[y*y for y in x])
plt.title("selectionsort ")
plt.xlabel("input")
plt.ylabel("time")
