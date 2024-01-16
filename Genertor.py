#decorator chaining:


#genertors:

l=[x*x for x in range(1,11)]
print(l)

l=[2*x for x in range(10)]
print(l[0])
print(l[1])
print(l[2])
print(l[3])

l=[2*x for x in range(100000000)]
print(l[0])
print(l[1])
print(l[2])
print(l[3])

l=(2*x for x in range(1000000))
print(type(l))

l=[2*x for x in range(100)]
print(type(l))


l=(2*x for x in range(1000000))
print(next(l))
print(next(l))

def mygen():
    yield "A"
    yield "B"
    yield "C"
g=mygen()
print(type(g))
print(next(g))
print(next(g))
print(next(g))

def mygen():
    yield "1"
    yield "2"
    yield "3"
g=mygen()
print(type(g))
print(next(g))
print(next(g))
print(next(g))

def countdown(num):
    print("start countdown")
    while num>0:
        yield num
        num=num-1
values=countdown(5)
for i in values:
    print(i)


def countdoen(num):
    print("start countdown")
    while num>0:
        yield num
        num=num-1
values=countdown(4)
for i in values:
    print(i)

def firstn(num):
    i=1
    while i<=num:
        yield i
        i=i+1
values=firstn(5)
print(type(values))
for i in values:
    print(i)


def secondn(num):
    i=1
    while i<=num:
        yield i
        i=i+1
values=secondn(4)
print(type(values))
for i in values:
    print(i)