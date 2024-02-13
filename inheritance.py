#single level inheritance
#multi level inheritance
#hierarchical inheritance
#multiple inheritance

#single level inheritance
class p:
    def m1(self):
        print("this is parent class")
class c(p):
    def m2(self):
        print("this is child class")
c=c()
c.m2()
c.m1()


class p():
    def first(self):
        print("this is a first function")
class c(p):
    def second(self):
        print("this is second function")
c=c()
c.first()
c.second()

class p():
    def a(self):
        print("this is a first section")
class c(p):
    def b(self):
        print("this is second section")
c=c()
c.a()
c.b()

#multi level inheritance
class gp:
    def m1(self):
        print("grand father")
class p(gp):
    def m2(self):
        print("parent")
class c(p):
    def m3(self):
        print("child")
c=c()
c.m1()
c.m2()
c.m3()



class organism:
    alive=True
class animal(organism):
    def eat(self):
        print("this animal is eating")
class dog(animal):
    def bark(self):
        print("this dog is barking")
dog = dog()
print(dog.alive)
dog.eat()
dog.bark()


class human:
    alive=True
class man(human):
    def eat(self):
        print("this human is eating")
class arjun(man):
    def silent(self):
        print("this man is silent")
arjun = arjun()
print(arjun.alive)
arjun.eat()
arjun.silent()


class gp:
    def m1(self):
        print("grand father")
class p(gp):
    def m1(self):
        print("parent")
class c(p):
    def m1(self):
        print("child")
c=c()
c.m1()

class gp:
    def m1(self):
        print("grand father")
class p(gp):
    def m1(self):
        print("parent")
class c(p):
    def m3(self):
        print("child")
c=c()
c.m1()


#hierarchical -> single parent but multiple child class

class mobile:
    def a(self):
        print("mobile")

class c1(mobile):
    def b(self):
        print("samsung")
        
class c2(mobile):
    def c(self):
        print("nokia")

c1=c1()
c1.b()
c1.a()
        
c2=c2()
c2.a()
c2.c()

class p:
    def m1(self):
        print("parent")

class c1(p):
    def m2(self):
        print("child 1")
        
class c2(p):
    def m3(self):
        print("child 2")

c1=c1()
c1.m2()
c1.m1()
        
c2=c2()
c2.m1()
c2.m3()


class human:
    def a(self):
        print("human")

class c1(human):
    def b(self):
        print("raja")
        
class c2(human):
    def c(self):
        print("rani")

c1=c1()
c1.a()
c1.b()
        
c2=c2()
c2.a()
c2.c()


class p:
    def a(self):
        print("parent")

class c1(p):
    def b(self):
        print("raja")
        
class c2(p):
    def c(self):
        print("rani")

c1=c1()
c1.a()
c1.b()
        
c2=c2()
c2.a()
c2.c()


#multiple #if parent class is multiple but one child class
class p1:
    def m1(self):
        print("parent")
class p2:
    def m2(self):
        print("parent 2")
class c(p1,p2):
    def m3(self):
        print("child")
c=c()
c.m2()
c.m1()
c.m3()
    

class p1:
    def a(self):
        print("parent")
class p2:
    def a(self):
        print("parent 2")
class c(p1,p2):
    def a(self):
        print("child")
c=c()
c.a()

class p1:
    def a(self):
        print("parent")
class p2:
    def a(self):
        print("parent 2")
class c(p1,p2):
    def b(self):
        print("child")
c=c()
c.a()
c.b()
    

class p1:
    def c(self):
        print("parent")
class p2:
    def a(self):
        print("parent 2")
class c(p1,p2):
    def b(self):
        print("child")
c=c()
c.a()
c.b()
c.c()
    