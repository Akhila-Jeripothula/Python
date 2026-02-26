#global and local variable
x="Akhila"
def mufunc():
    x="Akshaya"
    print("My name is",x)
mufunc()
print("My name is",x)

#data types
#type conversion
x=5.5
print(complex(x))

#strings
strr="Akhila is a good girl"
print("good" not in strr)

str="hello"
print(str[::-1])

a="akhila"
print(a.split())

b="Hello"
print("hii" .join(b))

#list
list=["apple","banana"]
list[1]="Mango"
print(list)
list.append("orange")
print(list)
list.insert(1,"kiwi")
print(list)
lost=["hi","Hello"]
list.extend(lost)
print(list)

list.remove("kiwi")
print(list)
list.pop(0)
print(list)
list.clear()
print(list)

list1=["apple","banana","grapes","cherry"]
list1.sort()
print(list1)
list2=list1[:]
print(list2)
list2=list1.copy()
print(list2)

#tuple
# x = ("apple", "banana", "cherry")
# y = list(x)
# y[1] = "kiwi"
# x = tuple(y)

# print(x)
tuple=("apple","banana","cherry")
(green,red,blue)=tuple
print(green)
print(blue)


#sets

# Access Items
# You cannot access items in a set by referring to an index or a key.
# But you can loop through the set items using a for loop, or ask if a specified value is present in a set, by using the in keyword.

thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)

thisset = {"apple", "banana", "cherry"}

print("banana" in thisset)


#dictionary:
thisdict={
   "name":"Akhila",
   "age":27
}
print(thisdict)
print(thisdict["name"])
x=thisdict.get("name")
print(x)

#key value pairs:
y=thisdict.keys()
print(y)
z=thisdict.values()
print(z)
a=thisdict.items()
print(a)

