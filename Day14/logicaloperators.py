# Logical Operators - and/or/not

#and
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")   #both conditions must be true


#or
a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True") # atleast one should be true


#not
a = 33
b = 200
if not a > b:
  print("a is NOT greater than b")