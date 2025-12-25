#Python Operators
#Operators are symbols that tell Python to perform an action on values or variables.
print(10+5)
print(100+12)

#Python divides the operators in the following groups:

# Arithmetic operators
# Assignment operators
# Comparison operators
# Logical operators
# Identity operators
# Membership operators
# Bitwise operators


#1.Arithematic Operators
x=15
y=4
print(x+y)#addition
print(x-y)#subtraction
print(x*y)#multiplication
print(x/y)#division
print(x%y)#modulous
print(x//y)#floor division(nearest number)
print(x**y)#exponential




#2.Assignment Operators(Used to assign values to variables)
a=10
a+=2
print(a)
# =		
# +=		
# -=	
# *=		
# /=		
# %=		
# //=		
# **=		
# &=	
# |=		
# ^=	
# >>=	
# <<=		
# :=(Walrus operator)



#3.Comparision Operators(compare two values)
a=10
b=5
print(a==b)
print(a!=b)
print(a<b)
print(a>b)
print(a<=b)
print(a>=b)
#gives boolean values
#Python allows chaining comparision operators
x=5
print(1<x<10)
print(1<x and x<10)



#4.Logical Operators(combine condition statements)
x=5
print(x>3 and x<10)#returns true if both statements are true
print(x>3 or x<4)#returns true if one statement is true
print(not(x>3 and x<10))

