

def aman(x):
    print("hii",x)
aman(10)
aman("raju")

def malli(i):
    if i%2==0:
        print("even")
    else:
        print("odd")

malli(11)


#factorial
def fact(x):
    a=1
    while x>0:
        a=a*x
        x=x-1
    return a
n=fact(5)
print(n)

def sam(a,b):
    sum=a+b
    sb=a-b
    mul=a*b
    return sum,sb,mul
l=sam(5,6)
for i in l:
    print(i)


#keywrd rguments
def key(name,no):
    print("Hii",name, no)

key(no=20,name="raju")

#positional arguments

def key(name,no):
    print("Hii",name, no)

key(20, "raju")

#default

def key(name,no, phno=134):
    print("Hii",name, no, phno)

key("raju", 20)

#variable legth

def len(*a):
    print("Hii", a)

len(10,20,30,40)

#local, global varbles
#global

a=10 
def fun1():
    print(a)
fun1()
#local
def fun2():
    a=20
    print(a)
fun2()
#global,local priority

a=20 
def fun():
    a=10
    print(a)
fun()


a=5
def var():
    a=10
    print("var",a)
def var1():
    global a
    print("var1",a)
var()
var1()

 #Built-in functions
     # id(), print(), type()
a=id(10)
print(a)
print(type(a))

c=20
id(a)
print(a)
print(type(a))

#user define functions:

import keyword
print(keyword.kwlist)


def wish():
    print("hello gud morning")
wish()

def wish():

    print("mallareddy")
wish()
wish()
wish()
wish()

#parameter:
#input to the fuction.

def wish(name):
    print("hello",name,"good mng")
wish("mallareddy")
wish("sunny")
wish("raju")



def wish(number):
    print("the square of",number,"is",number**3)
wish(3)
wish(4)

def wish(number):
    print("sum of",number,number+2)
wish(4)
wish(2)


#return statement:

def add(x,y):
    return x+y
result=add(10,20)
print("the sum is",result)
print("the sum is",add(20,30))

def add(a,b):
    return a+b
result=add(5,6)
print("sum of",result)
print("sum of",add(11,6))

def add(a,b):
    return a+b
print("sum of",add(11,6))

#example:
def f1():
    print("hi")
print(f1())

def f1():
    print("hi")
f1()
print(f1())

#Finding the even _odd numbers:
def even_odd(number):
    if number%2==0:
        print(number,"is even number")
    else:
        print(number,"is odd number")
even_odd(10)
even_odd(15)

def even_odd(number):
    if number%2==0:
        print(number,"is even number")
    else:
        print(number,"is odd number")
even_odd(2)
even_odd(3)

#factorial function
def fact(num):
    result=1
    while num>=1:
        result=result*num
        num=num-1
    return result
print(fact(5))

def fact(num):
    result=1
    while num>=1:
        result=result*num
        num=num-1
    return result
print(fact(3))

def fact(num):
    result=1
    while num>=1:
        result=result*num
        num=num-1
    return result
print(fact(7))

#factorial of 1 is:1
#facorial 2 is:2
def fact(num):
    result=1
    while num>=1:
        result=result*num
        num=num-1
    return result
for i in range (1,6):
    print("the factorial",i,"is:",fact(i))


    #returning multiple values from a function
    def sum_sub(a,b):
        sum=a+b
        sub=a-b
        return sum,sub
    c,d=sum_sub(10,20)
    print("sum is:",c)
    print("sub is:",d)

    def cal(a,b):
        sum=a+b
        sub=a-b
        div=a/b
        mul=a*b
        return sum,sub,div,mul
    x=cal(20,10)
    print(type(x))
    print("the result are:")
    for i in x:
        print(i)



        

