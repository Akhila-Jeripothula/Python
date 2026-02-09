#FUNCTIONS

#calling function
def greet():
    print("Hello, welcome to Python!")
greet()   


#using parameter
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
