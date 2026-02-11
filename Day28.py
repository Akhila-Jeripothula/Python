#return statement
# Instead of printing, we can return a value.
def add(a, b):
    return a + b

result = add(5, 3)
print(result)


#scope

# Where a variable can be accessed in the program.
#1.Local scope

  # A variable created inside a function.
  # It can be used only inside that function.

def myfunc():
    x=30
    print(x)
myfunc()
# print(x)   error


#2.Global scope:

# A variable created outside all functions.
# It can be accessed inside functions (but careful while modifying).

x = 20   
def test():
    print(x)
test()





x = 10
def test():
    x = 5   # This creates a new local variable
    print(x)
test()
print(x)


#global keyword-to modify
def myfunc():
  global x
  x = 300
myfunc()
print(x)

