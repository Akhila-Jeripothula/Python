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
print(not(x>3 and x<10))#reverse the result






#5.Identity Operators(Identity operators are used to check whether two variables refer to the SAME object in memory,not whether their values are equal.)
# 1.is	    (True if both variables point to the same object)
# 2.is not    (True if they point to different objects)

#1.is operator
x = ["apple", "banana"] #(new list object is created)
y = ["apple", "banana"] #(different new list object is created even though the values are different)
z = x     #(points to same object as x)

print(x is z)
print(x is y)
print(x == y)

#2.is not operator
x = ["apple", "banana"]
y = ["apple", "banana"]

print(x is not y)

#3.Difference between == and is
x = [1, 2, 3]
y = [1, 2, 3]

print(x == y)
print(x is y)




#6.Membership Operators(Membership operators are used to test if a sequence is presented in an object)
Flowers=["Roses","Lotus","Tulip","Orchids"]

print("Roses" in Flowers)            #in
print("Water lilly" in Flowers)      #in
print("Water Lilly" not in Flowers)  #not in




#7.Bitwise Operators(Bitwise operators work on binary numbers (0s and 1s))
# & 	AND		
# |	    OR	
# ^	    XOR	
# ~	    NOT		
# <<	left shift
# >>    right shift

# 6 = 0110
# 3 = 0011
# --------
# 2 = 0010 (&  both 1)
# 7 = 0111 (|  only 1 ot both 1)
# 5 = 0101 (^  only 1 )

print(6 & 3)
print(6 | 3)
print(6 ^ 3)





#Operator Precedence(Decides which operation python performs first)
print((6 + 3) - (6 + 3))#paranthesis high priority