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

