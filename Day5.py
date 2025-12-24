#Python Boolean(True/False)

#example 1(Comparing two values,return boolean answer)
print(10>9)
print(10==10)
print(10<9)
#example 2(when you run condition in if statement,returns boolean values)
#Print a message based on whether the condition is True or False: 
a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")


#evaluating value(bool())
x=5
print(bool(x))
print(bool(0))



#Function also returns boolean values
def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")


#Python has many built-in functions that return a boolean value (True or False).
#One commonly used function is isinstance().
x = 200
print(isinstance(x, int))
