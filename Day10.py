#Python Tuples(stores collection of values)
# A tuple is a collection which is ordered and unchangeable.(round brackets)
x=("apple","banana")
print(x)


#1.ordered(have definite order and it will not change)
#2.unchangeble(we cannot remove or add the items once a tuple is created)
#3.Allow Duplicate values(can have the same item multiple times)


#length of the tuple
print(len(x))

#one item in tuple-keep comma
y=("rose",)
print(type(y))

#Tuple can be of any datatype
tuple1 = ("apple", "banana", "cherry")   #string
tuple2 = (1, 5, 7, 9, 3)                 #int
tuple3 = (True, False, False)            #boolean
tuple4 = ("abc", 34, True, 40, "male")   #mic of all

#Access tuple items
thistuple = ("apple", "banana", "cherry","grapes","mango")
print(thistuple[1])
print(thistuple[-1])
print(thistuple[1:3])

#updating the tuple #first convert it into list
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
y.append("orange")
x = tuple(y)
print(x)

#unpacking
# When we create a tuple, we normally assign values to it. This is called "packing" a tuple:
fruits = ("apple", "banana", "cherry")
# But, in Python, we are also allowed to extract the values back into variables. This is called "unpacking":
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)

#Asterisk-If the number of variables is less than the number of values, you can add an * to the variable name and the values will be assigned to the variable as a list:

#Loop Tuples

# You can loop through the tuple items by using a for loop.
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)
#Loop through index number-(range,len)
thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])
#while loop-Use the len() function to determine the length of the tuple, then start at 0 and loop your way through the tuple items by referring to their indexes.
# Remember to increase the index by 1 after each iteration.
thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1
