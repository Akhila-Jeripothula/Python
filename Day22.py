#functions


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

def get_greeting():
  return "Hello from a function"

message = get_greeting()
print(message)