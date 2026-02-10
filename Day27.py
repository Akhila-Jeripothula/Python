#FUNCTIONS

#calling function
def greet():
    print("Hello, welcome to Python!")
greet()   


# parameter using:
def greet(name):
    print("Hello",name)
greet("Akhila")

#diff types of parameters

# 1.Positional
# 2. Keyword
# 3.Default
# 4.Variable-length (*args)
# 5.Keyword variable-length (**kwargs)

#1.positional
#order matters,basic
def sub(a, b):
    print(a - b)
sub(10, 5)      

#2.keyword
#pass values through parameters names
def sub(a,b):
    print(a-b)
sub(b=5,a=10)

#3.default parameter
#if a value is not used then a default one is passed
def greet(name="akhi"):
    print("Hello",name)
greet()
greet("Akhila")
#output
# Hello akhi
# Hello Akhila

#4.Variable Length parameters(*args)
#used when number of arguments is unknown
def add(*num):
    print(sum(num))
add(1,2,3,4)
#OUTPUT=10

#5. Keyword variable length parameters
#used when arguments are passed as key value pairs
def info(**data):
    print(data)
info(name="Akhila", age=21, course="Python")
#output:{'name': 'Akhila', 'age': 21, 'course': 'Python'}
