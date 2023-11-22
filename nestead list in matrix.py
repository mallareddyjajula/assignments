l1=[1,10,15,20,[2,3,-10],7,0]
#print(len(l1))
print(l1[4][2])
print(l1[len(l1)-2])
print(l1[1:6:2])
print(l1[2:7:1])

l=[[10,20,30],[40,50,60],[70,80,90]]
for i in range(len(l)):
    for j in range(len(l[i])):
        print(l[i][j],end=" ")
    print("\n")

l=[1,2,3],[4,5,6],[7,8,9]
for i in range(len(l)):
    for j in range(len(l[i])):
        print(l[i][j],end=" ")
    print("\n")   

