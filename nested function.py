def outer():
    print("outer function started")
    def inner():
        print("inner function started")
    print("outer function returning inner function")
    return inner
f1=outer()
f1()
f1()
    
def calc():
    print("i am calc function")
    def add():
        print("i am add function")
    return add()
add_ref=calc()
print(add_ref)

def multi(a):
    def mul(b):
        def mu(c):
            return a*b*c
        return mu
    return mul
y=multi(10)(30)(2)
print(y)
   