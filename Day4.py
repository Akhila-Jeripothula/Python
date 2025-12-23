#Python DataTypes(Strings)

#1.Python Declaration
x="String"
print(x)


#multiline string
a="""This is Akhila,
from Bhoj Reddy colleg"""
print(a)

#Charecter at position 
a="Akhila"
print(a[1])

#loops in strings(python uses indentation only in conditional statements and loops)
for x in "banana":
    print(x)

#length of the string
a = "Hello, World!"
print(len(a))

#Check String or not(keywod=in)
txt = "The best things in life are free!"
print("free" in txt)

txt = "The best things in life are free!"
print("expensive" not in txt)






#2.Slicing String(Extracting a part of string)
a="Akhila"
print(a[2:5])
print(a[:5]) #prints starting index
print(a[2:]) #prints endind index
print(a[-2:-5]) #negatice index






#3.modifying Strings(upper,lower,strip,split,replace)
x="    Akhila , j   "
print(x.upper())
print(x.lower())
print(x.strip())#removes white spaces
print(x.split(","))
print(x.replace("A","W"))





#4.String concatenation(Joining/Combining)
a="akhila"
b="jeripothula"
c=a+b
print(c)
print(a+""+b)


