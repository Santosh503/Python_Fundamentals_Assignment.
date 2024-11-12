a=10
print("a=",type(a))
b=20.5
print("b=",type(b))
c="Hello World."
print("c=",type(c))
d=True
print("d=",type(d))

print("a*a=",a*a)
print("b/a=",b/a)

if d:
    print("It's True") #use of boolean
else:
    print("It's False")

print(c+" I hope you are fine. "+ "My age is "+str(a)) # use of concatination

if a>b:
    print("a is older than b") #logical operations
else:
    print("b is older than a")

dictionary={            #dictionary
    "Name":"Hari",
    "Age":28,
    "email":"hari@gmail.com"
}

print(dictionary)      #printing dictionaries

for key,values in dictionary.items():     #printing keys, values in dictionary
    print(key ,end=" ")
    print(values,end=" ")