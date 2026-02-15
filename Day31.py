


#1.even or odd:

def check_even_odd(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"

print(check_even_odd(7))




#2.largest no:

def largest(a, b):
    if a > b:
        return a
    else:
        return b

print(largest(10, 25))


#3.reverse of string
def reverse_string(s):
    return s[::-1]

print(reverse_string("Python"))

#count vowels:
def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

print(count_vowels("Akhila"))


#5.args
def sum_numbers(*args):
    total = 0
    for num in args:
        total += num
    return total

print(sum_numbers(1, 2, 3, 4))







