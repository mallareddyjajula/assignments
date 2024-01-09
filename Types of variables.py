#Types of variables:
#global variable:
#local vaiable:

a=10 #global variable
def f1():
    print("f1:",a)
def f2():
    print("f2:",a)
f1()
f2()

a=10
def f1():
    a=20 # local variable
    print("f1:",a)
def f2():
    print("f2:",a)
f1()
f2()

a=30
def f1():
    global a
    a=25
    print("f1:",a)
def f2():
    print("f2:",a)
f1()
f2()

b=10
def f1():
    global b
    b=40
    print("f1:",b)
def f2():
    print("f2:",b)
f1()
f2()

b=10
def f1():
    global b
    b=40
    print("f1:",b)
def f2():
    print("f2:",b)
f2()
f1() 

b=10
def f1():
   b=30
   print("f1:",b)
f1()

b=9
def f1():
   b=33
   print("f1:",b)
   print(globals()['b'])
f1()

#recursive functions:

def factorial(n):
    if n==0:
        result=1
    else:
        result=n*factorial(n-1)
    return result
print("factorial of 6 is:",factorial(6))
print("factorial of 0 is:",factorial(0))

def factorial(n):
    if n==0:
        result=1
    else:
        result=n*factorial(n-1)
    return result
print("factorial of 5 is:",factorial(5))
print("factorial of 4 is:",factorial(4))
print("factorial of 3 is:",factorial(3))

#anonymous function:
#normal functin:
def squareit(n):
    return n*n
#syntax of lambda function
  # lambda argument_list:expression
s=lambda n:n*n
print("the square of 3 is:",s(3))
print("the square of 5 is:",s(5))

#lambda function to find sum of 2 given numbers
s=lambda a,b:a+b
print("the sum of 3,2 is:",s(3,2))
print("the sum of 3,7 is:",s(3,7))

#lambda function to find sub of  given numbers

s=lambda a,b:a-b
print("the sum of 3,2 is:",s(3,2))
print("the sum of 3,7 is:",s(3,7))

#lambda function to find biggest of 2 given numbers
s=lambda a,b:a if a>b else b
print("the biggest of 10,20 is:",s(10,20))
print("the biggest of 30,20 is:",s(30,20))

#lambda function to find lowest of 2 given numbers
s=lambda a,b:a if a<b else b
print("the biggest of 10,20 is:",s(10,20))
print("the biggest of 30,20 is:",s(30,20))

#filter function:
#syn:
#filter(function,sequence)
#without lambda function

def is_even(n):
    if n%2==0:
        return True
    else:
        return False
l=[0,5,10,15,20,25,30]
print(type(filter(is_even,l)))
l1=list(filter(is_even,l))
print(l1)

#with lambda function
l=[0,5,10,15,20,25]
l1=list(filter(lambda x:x%2==0,l))
print(l1)
l2=list(filter(lambda x:x%2!=0,l))
print(l2)

#map function
l=[1,2,3,4,5]
def doubleit(x):
    return 2*x
l1=list(map(doubleit,l))
print(l1)

 
l=[1,2,3,4,5]
l1=list(map(lambda x:x*x,l))
print(l1)

#reduce function:
from functools import*
l=[10,20,30,40]
result =reduce(lambda x,y:x+y,l)
print(result)







