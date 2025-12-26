#Python has 4 built-in Datatypes for collection of data(list,tuple,set,Dictionary)
#Python Lists
  #Lists have square brackets
  #Lists store multiple items in a single variable
x=["Roses","lotus","lily","sunflower","orchids","hydranges"]
print(x)



#Charecterestics of lists-ordered,changeble,indexed,allows duplicate values
#1.ordered(Items have defined order,they will not change, new items will add at the end)
#2.changeble(we can change,add,remove items in list)
#3.Allows Duplicate Values(since lists are indexed they can have same values in list)
y=["apple","banana","apple"]
print(y)



#List Length
y=["apple","banana","apple"]
print(len(y))



#List datatypes(can be of anytype string,int,boolean or mix of all)
list1 = ["abc", 34, True, 40, "male"]
print(list1)


# From Python's perspective, lists are defined as objects with the data type 'list':
mylist = ["apple", "banana", "cherry"]
print(type(mylist))


#List Constructor
thislist=list(("apple","banana"))
print(thislist)



# Python Collections (Arrays)
# There are four collection data types in the Python programming language:

# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# Dictionary is a collection which is ordered** and changeable. No duplicate members.
