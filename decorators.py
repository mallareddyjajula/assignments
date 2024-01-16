def wish(name):
    print("hello",name,"gud mng")
wish("mallareddy")
wish("arjun")
wish("raju")

def wish(message):
    print("hell",message,"reddy")
wish("gud mng")
wish("gud afternoon")
wish("gud evening")

def decor(func):
    def inner(name):
        if name=="sunny":
            print("hello sunny very very gud mng")
        else:
            func(name)
    return inner
#@decor
def wish(name):
    print("hello",name,"gud mng")
decorfunction=decor(wish)
decorfunction("bunny")
decorfunction("rani")

def decor(func):
    def inner(name):
        if name=="mallareddy":
            print("hi mallareddy very very good evening")
        else:
            func(name)
    return inner
@decor
def wish(name):
    print("hi",name,"good evening")
wish("latha")
wish("madhu")
wish("malli")

def decor(func):
    def inner(name):
        if name=="latha":
            print("hi latha good after noon")
        else:
            func(name)
    return inner
@decor
def wish(name):
    print("hi",name,"gud after noon")
decorfunction=decor(wish)
decorfunction("rani")
decorfunction("siri")
decorfunction("manish")

def decor(func):
    def inner(name):
        if name=="animi":
            print("hi animi how are you")
        else:
            func(name)
    return inner
@decor
def wish(name):
    print("hi",name,"how are you")
decorfunction=decor(wish)
wish("raju")
wish("sreenu")
wish("prabha")


def division(a,b):
    return a/b
print(division(10,5))
#print(division(10,0))
print(division(10,2))

def smart_division(func):
    def inner(a,b):
        print("we are dividing",a,"with",b)
        if b==0:
            print("oop's...can't divided with zero")
        else:
            return func(a,b)
    return inner
@smart_division
def division(a,b):
    return a/b
print(division(10,5))
print(division(10,0))
print(division(10,2))

def decor(func):
    def inner():
        x=func()
        return x*x
    return inner
def decor1(func):
    def inner():
        x=func()
        return 2*x
    return inner
@decor
@decor1
def num():
    return 10
print(num())


def decor(func):
    def inner():
        a=func()
        return a*a
    return inner
def decor1(func):
    def inner():
        a=func()
        return 2*a
    return inner
@decor
@decor1
def num():
    return 30
print(num())


