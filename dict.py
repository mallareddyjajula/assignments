a=10
b=20
a=a+b
b=a-b
a=a-b
print(a)
print(b)

a,b="pq"
b,c="qr"
print(a,b,c)

d={100:"malla",200:"raju",300:"sreenu"}
d[400]="sathish",
d[40]="rani",
del d[200]
d.clear()
print(d)


list=["ram","raj","malla"]
d={100:list}
print(d)
l=["rami","anji","animi"]
d={200:l}
print(d)

#imp function of dict
d=dict()
print(type(d))
d=dict([(100,"raj"),(200,"anji"),(300,"animi")])
print(d)
print(d.get(100))
d=dict({(100,"raj"),(200,"anji"),(300,"animi")})
print(d.get(100))
print(d)
d=dict(((100,"raj"),(200,"anji"),(300,"animi")))
print(d)
print(d[100])
#d={100:"raj",200:"anji",300:"animi"}
#d[100]
print(d)
d=dict({100:"raj",200:"anji",300:"animi"})
print(d)
print(d[100])
#pop()
print(d.pop(100))
print(d)
#popitem()
d=dict({100:"raj",200:"anji",300:"animi"})
print(d.popitem())
print(d.popitem())
print(d.popitem())
print(d)
#keys,values,itemsm
d=dict({100:"raj",200:"anji",300:"animi"})
print(d.keys())
print(d.values())
print(d.items())
#len,clear
d=dict({100:"raj",200:"anji",300:"animi"})
print(len(d))
print(d[200])
print(d.get(100))
print(d.get(400,"sita"))
print(d.clear())

#program1
d=dict({100:"raj",200:"anji",300:"animi"})
l=d.items()
for k,v in l:
    print("keys are",k,"values are", v)

#program2
d=dict({100:"raj",200:"anji",300:"animi"})
a=d.keys()
b=d.values()
for j in a:
    print("key",j,end=" ")
for i in b:
    print("value",i,end=" ")
