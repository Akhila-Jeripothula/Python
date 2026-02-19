#FUNCTIONS

def changecase(func):
  def myinner():
    return func().upper()
  return myinner

@changecase
def myfunction():
  return "Hello"

@changecase
def otherfunction():
  return "I am Akhila!"

print(myfunction())
print(otherfunction())