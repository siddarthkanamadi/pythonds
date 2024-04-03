class student:
    def __init__ (self,name,rollno,marks1,marks2,marks3):
        self.name=name
        self.rollno=rollno
        self.marks=[]
        self.marks.append(marks1)
        self.marks.append(marks2)
        self.marks.append(marks3)
        
    def display(self):
        print("Student Details Are")
        print("Name :",self.name)
        print("Roll Number :",self.rollno)
        print("Marks Of Student Are :",self.marks)
        
    def getmarks(self):
        return self.marks
