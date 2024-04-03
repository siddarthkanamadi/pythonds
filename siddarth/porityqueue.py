class priortiyqueue:
    def __init__(self):
        self.queue=[]
    def display(self):
        print(self.queue)
    def isempty(self):
        return len(self.queue)==0
    def insert(self,data):
        self.queue.append(data)
    def delete(self):
        max_val=0
        for i in range(len(self.queue)):
            if self.queue[i]>self.queue[max_val]:
                max_val=i
        item=self.queue[max_val]
        del self.queue[max_val]
        return item
    
myqueue=priortiyqueue()
myqueue.insert(10)
myqueue.insert(1)
myqueue.insert(20)
print(myqueue.display())
while not myqueue.isempty():
    print(myqueue.delete())
