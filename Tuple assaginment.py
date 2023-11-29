'''a=(10,20,30,4,50)
print(len(a))a.count(10)
print()
print(a.index(4))
print(type(a))
print(sorted(a))
#print(a(sorted))

#tuple packing and unpacking

a=10
b=20
c=30
d=40
e=a,b,c,d
print(type(e))
a,b,c,d=e
print(e)
print("a",a,"b",b,"c",c,"d",d)
print(type(a))

#min() and max():
t=(70,80,10,40)
print(len(t))
print(max(t))
print(min(t))

t="mallareddy"
print(len(t))
print(min(t))
print(max(t))

#sorted()
t=(50,30,10,40,20)
a=sorted(t)
print(a)'''

#len():
t=(10,20,30,40)
print(len(t))

t="malla reddy"
print(len(t))

t="mallareddy"
print(len(t))

#count():
t=(10,20,30,40,50)
print(t.count(20))

#index():
t=(10,20,30,40,50)
print(t.index(50))