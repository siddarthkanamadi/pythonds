from stu_adt import*
import time
from sys import getsizeof
start_time=time.time()

s1=student("Soheb",1,98,89,95)
s2=student("Siddarth",5,98,97,96)
s3=student("Sujan",6,95,94,93)

s1.display()
studentmarks=s1.getmarks()
average=sum(studentmarks)/len(studentmarks)
print("Average Marks Of Student Is ",average)

s2.display()
studentmarks=s2.getmarks()
average=sum(studentmarks)/len(studentmarks)
print("Average Marks Of Student Is ",average)
s2.display()

s3.display()
studentmarks=s3.getmarks()
average=sum(studentmarks)/len(studentmarks)
print("Average Marks Of Student Is",average)

print("Space taken by program ",getsizeof(s1)+getsizeof(s2)+getsizeof(s3))
print("Time taken by program is ",(time.time()-start_time))    

