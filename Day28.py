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