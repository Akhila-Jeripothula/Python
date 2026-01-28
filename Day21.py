# for loop
# num = int(input("Enter number: "))
# for i in range(1, 11):
#     print(f"{i} * {num} = {num*i}")



#factorial
# num = int(input("Enter the number: "))
# fact = 1

# for i in range(1, num+1):
#     fact *= i


# print("Factorial", fact)


#prime
num = int(input("Enter number: "))
flag = True

for i in range(2, num):
    if num % i == 0:
        flag = False
        break

if flag and num > 1:
    print("Prime")
else:
    print("Not Prime")

