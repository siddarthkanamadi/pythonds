q=[]
def enqueue():
    if len(q)==size:
        print("queue if full!!!")
    else:
        element=input("enter the element")
        q.append(element)
        print(element,"is added to the queue!")
def dequeue():
    if not q:
        print("qeueue is empty!!")
    else:
        e=q.pop(0)
        print("element removed !!",e)
def display():
    print(q)

size=int(input("enter the number :"))
while True:
    print("select the opertions 1.add 2.delete 3.dispaly 4.quit")
    choice=int(input("enter the number "))
    if choice==1:
        enqueue()
    elif choice==2:
        dequeue()
    elif choice==3:
        display()
    elif choice==4:
        break
    else:
        ("invalid option")
