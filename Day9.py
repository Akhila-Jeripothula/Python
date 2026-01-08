#List Comprehension(short syntax)
# Based on a list of fruits, you want a new list, containing only the fruits with the letter "a" in the name.
# Without list comprehension you will have to write a for statement with a conditional test inside:

fruits = ["apple", "banana", "cherries", "kiwi", "mango"]#for loop
newlist = []
for x in fruits:
  if "a" in x:
    newlist.append(x)
print(newlist)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]#list comprehension
newlist = [x for x in fruits if "a" in x]
print(newlist)



#Sorting the list
x=["apple","pineapple","kiwi","orange","custardapple","mango"]   #sort alphabetically
y=[23,32,12,15,2,48,31]                                          #sort numerically
x.sort()
y.sort()
print(x)
print(y)
x.sort(reverse=True)       #sort in Descending order
print(x)
x.reverse()                #sort in reverse order
print(x)



#copy list
# Make a copy of a list with the copy() method:
a=["rose","tulip"]
mylist=a.copy()
print(mylist)


#Joining list
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)
