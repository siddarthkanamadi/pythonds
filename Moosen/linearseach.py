import matplotlib.pyplot as plt
def liner_search(array,key):
    n=len(array)
    for i in range(n):
        if array[i]==key:
            return True
        else:
            return False
        
array=[10,20,30]
key=30
if liner_search(array,key):
    print("target value is found")
else:
    print("ele is not found")

x=list(range(1,1000))
plt.plot(x,[y for y in x])
plt.title("linaeseacrh")
plt.xlabel("input")
plt.ylabel("time")
plt.show()