#Python Data Types

 #1.Int-whole numbers(no decimals) x=32
 #2.float-Decimal numbers  price=40.2
 #3.string-text/charecters(always in "")  name="akhila"
 #4.boolean-True/false   is_student=true



#how to get data type
x=10
print(type(x))


price=32.5
print(type(price))


#Integer Data type
#1.printing an integer 
y=10
print(x)

#2.Addition of two integers
a=20
b=30
print(a+b)

#3.Square of two integers
n = 5
print(n * n)

#4.swapping of two integers
a = 10
b = 20

a, b = b, a
print(a, b)

#5.Check even or odd
num = 7

if num % 2 == 0:
    print("Even")
else:
    print("Odd")



#Float Data Type
#1.printing float value
x = 3.5
print(x)

#2.Adding two float
a = 2.5
b = 1.2
print(a + b)

#3.Average of two float
a = 10.5
b = 20.5
average = (a + b) / 2
print(average)

#4.convering kilometers to meters
km = 2.5
meters = km * 1000
print(meters)

#5.Area of triangle
b=5.2
h=4.8
area=(1/2*b*h)
print(area)





#Type Conversion
#Converting one data type to another datatype
s=10
t=2.5
s=float(s)
t=int(t)
