#Types of Arguments:
#positional argumts:
def sub(a,b):
    print(a-b)
sub(100,200)
sub(20,10)

#def sub(a,b):
    #print(a-b)
#sub(10,20,5) # type error

def add(a,b):
    print(a+b)
add(10,20)

def mul(a,b):
    print(a*b)
mul(2,3)

def div(a,b):
    print(a/b)
div(2,3)

def div(a,b,c):
    print(a*b*c)
div(2,3,4)


#keyword arguments:
def wish(name,msg):
    print("hello",name,msg)
wish("nag","gud mng")

def wish(name,msg):
    print("hello",name,msg)
wish(name="raju",msg="gud mng")
wish(msg="love you",name="madhu")

def wish(name,msg):
    print("hi",name,msg)
wish("malli","gud af noon")#valid
wish(name="rani",msg="gud af noon")#valid
wish("malli",msg="gud af noon")#valid
#wish(name="malli","gud af noon")#invalid

def wish(name):
    print("hi",name,"darling")
wish("latha")

def wish(msg):
    print("sitha",msg)
wish("love you")

#default arguments:
def wish(name="malli"):
    print("hello",name,"gud mng")
wish("raju")

def wish(name="raju",msg="gud ofter noon"):
    print("hi",name,msg)
wish("raju")   
wish("rani")
wish("subbu")
wish("lakshmi")

#variable arguments:
#def sum(n1,n2):
#def sum(n1):
def sum(*n):
    total=0
    print("sum of:",total)
sum()

def sum(*n):
    total=1
    print(type(n))
sum()
 
def sum(*n):
    total=1
    print("sum of:",total)
sum()

def sum(*n):
    total=0
    print("sum of:",total)
sum()
sum(10)
sum(10,20)
sum(10,20,30)
sum(10,20,30,40)

def sum(*n):
    total=0
    for i in n:
        total=total+i
    print("sum is:",total)
sum()
sum(10)
sum(10,20)
sum(10,20,30)
sum(10,20,30,40,50)

def sum(*n):
    total=0
    for i in n:
        total=total+i
    print("sum is:",total)
sum()
sum(10)
sum(10,20)
sum(10,20,30)

def f1(n1,*s):
    print(n1)
    for i in s:
        print(i)
f1(10,20)

def f1(n1,*s):
    print(n1)
    for i in s:
        print(i)
f1(10,"A",20,"B")



    

    