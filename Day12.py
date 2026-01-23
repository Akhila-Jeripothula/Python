#Dictionaries


#Dictionaries are used to store values in key:value pairs
#Ordered changeable and do not allow duplicate variables(in python 3.7-ordered)
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print(thisdict["brand"])  #accsessing key values for python



#Do not allow duplicates
x={
  "name":"Akhila",
  "Year":3,
  "branch":"cse",
  "branch":"csm"
}
print(x)



print(len(x))#length of dictionary




#dictionary can be of any data types



#Dict constructor-we can use the dict constructor in dictionary
y=dict(name="akhila",age=19,branch="cse")
print(y)


#Accessing values

student={
    "name":"akhila",
    "age":36,
    "marks":370
}
print(student["name"])        #accessing normally
print(student.get("age"))     #accessing using get keyword
print(student.get("marks")) 



student["college"]="BRECW"    #adding values

student["age"]=21             #updating values

student.pop("age")




# pop(key)   	Removes specific key
# popitem()  	Removes last item
# del	        Deletes key or dict
# clear()	    Empties dict





#loop
for key in student:           #only key 
    print(key)
for x in student.values():    #only values
    print(x)
for x,y in student.items():   #both keys and values
    print(x,y)



#copy of dictionaries
newstudent=student.copy()
print(newstudent)

new_student=dict(student)
print(new_student)



#nested dictionaries
myfamily = {
  "child1" : {
    "name" : "sunny",
    "year" : 2004
  },
  "child2" : {
    "name" : "funny",
    "year" : 2007
  },
  "child3" : {
    "name" : "bunny",
    "year" : 2011
  }
}

print(myfamily["child2"]["name"])

#methods-keys,values,update,items -----
