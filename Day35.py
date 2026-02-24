#recursion

# Recursion is when a function calls itself to solve a smaller version of the same problem.

# Instead of using loops (for, while), the function repeats itself.

#1.factorial
# base case and recursive case:
def factorial(n):
    if n == 1:          # Base case
        return 1
    else:
        return n * factorial(n - 1)   # Recursive case

print(factorial(5))


#fibonacci:
def fibonacci(n):
    if n <= 1:   # Base case
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(6))


#3.countdown
def countdown(n):
    if n == 0:
        print("Done!")
        return
    print(n)
    countdown(n-1)

countdown(5)


#difference between recursion and loop

# | Recursion                 | Loop                         |
# | ------------------------- | ---------------------------- |
# | Calls itself              | Uses for/while               |
# | Cleaner for tree problems | Better for simple repetition |
# | Uses more memory          | Uses less memory             |
