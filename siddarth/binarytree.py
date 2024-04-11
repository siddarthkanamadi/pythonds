#skilltest no.2
class BST:
    def __init__(self,key):
        self.key=key
        self.lchild=None
        self.rchild=None
    def insert(self,data):
        if self.key is None:
            self.key=data
            return
        if self.key==data:
            return
        if self.key>data:
            if self.lchild:
                self.lchild.insert(data)
            else:
                self.lchild=BST(data)
        else:
            if self.rchild:
                self.rchild.insert(data)
            else:
                self.rchild=BST(data)
#
    def preorder(self):
        print(self.key)
        if self.lchild:
            self.lchild.preorder()
        if self.rchild:
            self.rchild.preorder()
#
    def inorder(self):
        if self.lchild:
            self.lchild.inorder()
        print(self.key)
        if self.rchild:
            self.rchild.inorder()
#
    def postorder(self):
        if self.lchild:
            self.lchild.postorder()
        if self.rchild:
            self.rchild.postorder()
        print(self.key)

    def search(self,val):
        if val<self.key:
            if self.lchild is None:
                return str(val)+"is not found"
            return self.lchild.search(val)
        elif val>self.key:
            if self.rchild is None:
                return str(val)+"is not found"
            return self.rchild.search(val)
        else:
            return str(self.key)+"is found"

root = BST(None)
list1=[10,7,6,8,13,12,14]
for i in list1:
    root.insert(i)
print("\n VALUES INSERTED SUCCESSFULLY")
print("\n == PRE-ORDER FASHION == ")
root.preorder()
print("\n == IN-ORDER FASHION == ")
root.inorder()
print("\n == POST-ORDER FASHION == ")
root.postorder()
print("\n == BINARY TREE SEARCH OPERATION == ")
print(root.search(100))
print(root.search(6))     
            


        