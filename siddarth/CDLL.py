class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class linkedlist:
    def __init__(self): 
        self.head=None
    def printlist(self):
        temp=self.head
        if(temp !=None):
            print("the list contains:",end="")
            while(True):
                print(temp.data,end="")
                temp=temp.next
                if(temp==self.head):
                    break
            print()
        else:
            print("the list is empty")

mylsit=linkedlist()
frist=Node(10)
mylsit.head=frist
frist.next=mylsit.head
mylsit.head.prev=frist
print()
second=Node(20)
second.prev=frist
frist.next=second
second.next=mylsit.head
mylsit.head.prev=second
print()
third = Node(30)
third.prev = second
second.next = third
third.next = mylsit.head
mylsit.head.prev = third
mylsit.printlist()
