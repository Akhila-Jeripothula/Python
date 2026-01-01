#SETS(store multiple values)

# A set is a collection which is unordered, unchangeable*, and unindexed(no duplecate values).
thisset = {"apple", "banana", "cherry"}    #curly braces
print(thisset)

#length of string
thisset = {"apple", "banana", "cherry"}
print(len(thisset))

#Can be of any data type
set1 = {"abc", 34, True, 40, "male"}

#type
myset = {"apple", "banana", "cherry"}  #set is the datatype
print(type(myset))



#Access Items
thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)



thisset = {"apple", "banana", "cherry"}
print("banana" in thisset)

thisset = {"apple", "banana", "cherry"}
print("banana" not in thisset)


#Add Itemss
thisset = {"apple", "banana", "cherry"}      #add
thisset.add("orange")
print(thisset)


thisset = {"apple", "banana", "cherry"}      #update
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)


#Remove
#remove item -remove or discard
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)


thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)

#remove-random item
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)
print(thisset)

#empty set-clear
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)

#delete set completely
thisset = {"apple", "banana", "cherry"}
del thisset
print(thisset)



#loop-for
y = {"apple", "banana", "cherry"}
for x in y:
  print(y)
