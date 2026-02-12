#PYTHON FUNCTIONS-RECURSION

#A recursive function is a function that solves a problem by calling itself.

#1. factorial
def factorial(n):
    if n == 1:           # Base case
        return 1
    else:
        return n * factorial(n - 1)   # Recursive case
print(factorial(5))

#output:120

#2.
def print_numbers(n):
    if n == 0:
        return
    print(n)
    print_numbers(n - 1)

print_numbers(5)



