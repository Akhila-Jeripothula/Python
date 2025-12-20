#python indentation
if 5>2:
    print("five is greater")

#wrong indentaion
if 5>2:
print("five is greater")
      

    



#python variables
x=20
x="Akhila"
print(x)

x=5
y="hello"
print(type(x))
print(type(y))

#assinging multiple variables
a,b,c=1,2,3
x=y=z=3
print(a)
print(b)
print(c)
print(x)
print(y)
print(z)

#pthon variable names rules
#1.must start with letter or undescore
#2.can contain letters,underscore,numbers but not special charecter like hyphen
#3.case sensitive
#4.cannot use python key words
#camelcase
#pascal case
#snake case

#Global variable and Local variable
x = "awesome"   # Global variable

def myfunc():
    x = "fantastic"   # Local variable
    print("Python is " + x)

myfunc()
print("Python is " + x)





