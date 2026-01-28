#functions(Basics)


# function is a block of code which only runs when it is called
# avoid code repetition

#1.creating function:

#function is defined using def keyword

def myfunc():
    print("hello world")

#calling function
def myfunc():
    print("hello world")
myfunc()

#calling function multiple times
def myfunc():
    print("hello world")
myfunc()
myfunc()
myfunc()
myfunc()
myfunc()
myfunc()

#Rules for function names
# func names are written same as var name
# 1.A function name must start with a letter or underscore
# 2.A function name can only contain letters, numbers, and underscores
# 3.Function names are case-sensitive (myFunction and myfunction are different)


#return statement
def get_greeting():
  return "Hello from a function"

message = get_greeting()
print(message)




def get_greeting():
  return "Hello from a function"

print(get_greeting())


# #pass
# generally function should not be empty so if you want it to be empty we should use pass statement:

def akhi():
   pass


#more than one return
def akhii():
   return 5
   return 10
print(akhii())

#Python arguments:
def greet(name):      # name → parameter
    print("Hello", name)

greet("Akhila")       # "Akhila" → argument



#diff types of arguments
