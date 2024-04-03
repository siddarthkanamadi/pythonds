import matplotlib.pyplot as plt
def bubblesort(array):
      for i in range (len(array)):
            for j in range(0,len(array)-i-1):
                  if array[j] > array[j+1]:
                      temp=array[j]
                      array[j]=array[j+1]
                      array[j+1]=temp
array=[50,40,30,20,10]
bubblesort(array)
print("Sorted Array in Ascending Order ")
print(array)

x=list(range(1,10000))
plt.plot(x, [y*y for y in x])
plt.title("Bubble Sort - Time Complexity is O(n\u00b2)")
plt.xlabel("Input")
plt.ylabel("Time")
plt.show()
