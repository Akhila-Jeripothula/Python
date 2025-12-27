#Access List Items
thislist = ["apple", "banana", "cherry"]
print(thislist[1])




#Range of indexes
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])




#Check if Items exist 
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")



#Change Item Value
list=["apple","banana","grapes","watermelon","mango"]
list[1]="cherry"
list[2:4]=["kiwi","strawberry"] #Change range
print(list)



# Insert Items
# To insert a new list item, without replacing any of the existing values, we can use the insert() method.
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)#watermelon will be added to the list at 2 position



#Add Items


# Append Items
# To add an item to the end of the list, use the append() method:
list=["apple","grapes"]
list.append("orange")
print(list)


# Insert Items
# To insert a list item at a specified index, use the insert() method.
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)


# Extend List
# To append elements from another list to the current list, use the extend() method.
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)


#Remove Item

# The remove() method removes the specified item.
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

# The pop() method removes the specified index.
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

thislist = ["apple", "banana", "cherry"]
del thislist #cause error

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist) #empties list



#Loop List
# You can loop through the list items by using a for loop:
x=["roses","lilly","orchids"]
for y in x:
 print(y)

# You can also loop through the list items by referring to their index number.(use range and len)
x = ["apple", "banana", "cherry"]
for i in range(len(x)):
  print(x[i])

# You can loop through the list items by using a while loop
y = ["apple", "banana", "cherry"]
i = 0
while i < len(y):
  print(y[i])
  i = i + 1

#List Comprehension(short)
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]
