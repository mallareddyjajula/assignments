'''class vaccine:
    name="vaccine"

    def show(self):
        print("inside vaccine class")
class covisheield(vaccine):
    gap=3
    def show(self):
        print("inside covishield class")
obj=covisheield()
print(obj.gap)
print(obj.name)
obj.show()
obj.show()


class vehicle:
    name="vehicle"
    def show(self):
        print("vehicle class")
class rangerover(vehicle):
    gap=3
    def show(self):
        print("rangerover class")
obj=rangerover()
print(obj.gap)
print(obj.name)
obj.show()
obj.show()

class employ:
    name="employ"
    def show(self):
        print("empoly class")
class python(employ):
    gap=1
    def show(self):
        print("python class")
obj=python()
print(obj.gap)
print(obj.name)
obj.show()
obj.show()

class student:
    name="student"
    def show(self):
        print("student class")
class python(student):
    gap=3
    def show(self):
        print("python class")
obj=python()
print(obj.gap)
print(obj.name)
obj.show()
obj.show()


class student:
    sname="varshitha"
    def __init__(self,name,section,rollno):
        self.name=name
        self.section=section
        self.rollno=rollno
    def display(self):
        print(self,name,"....",self,section,"....",self,rollno,".....")

#s=student()
#print(s.name)
#print(s.name)
s=student("animi","c",5)
s=student("varshitha","e",7)
s=student("raj","a",1)'''


class student:
    sname="varshitha"
    def __init__(self,empname,empphno):
        self.empname=empname
        self.empphno=empphno
    def display(self):
        print(self,empname,"....",self,empphno,)
s=student
s=student("varshitha",954240)
s=student("mallireddy",6987)
print(s.empname)
print(s.empphno)











     



 

