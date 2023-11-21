#string data type:
#There is no char data type

#printing strings
s='a'
s1='mallareddy'
s2="mallareddy"
print(type(s))
print(type(s1))
print(type(s2))

#slicing operatins:

s=input('enter any string:')
print('last character:',s[-1])
print('last but one character:',s[-2])

s1="0123456789"
print(s1[2:8:1])

print(s1[-1:-6:-1])
#capitlize
s='python session'
print(s.capitalize())
s='Python Session'
print(s.capitalize())


#title
name="python session"
print(name.title())
name="pYthOn sEsSion"
print(name.title())

#upper
s='mallareddy'
print(s.upper())


#lower
s='MALLAREDDY'
print(s.lower())

#swapcase
s='MALLAreddy'
print(s.swapcase())

a=input("enter some string")
i=0
for x in a:
    print("the char present at +ve index{} and -ve index{} is {}".format(i,i-len(a),x))
    i=i+1