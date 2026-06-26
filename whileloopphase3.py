# Phase 3 Topics
# 1.Armstrong Number
# 2.Strong Number
# 3.Perfect Number (revision)
# 4.Fibonacci sequence


#1.ARMSTRONG NUMBER:
# n=407
# original=n
# total=0
# while n>0:
#     digit=n%10
#     n=n//10
#     total=total+digit**3
# if(total==original):
#     print("Armstrong number")
# else:
#     print("Not an Armstrong Number")


#2.FIBONACCI:
# n=7
# a=0
# b=1
# count=1
# while count<=n:
#     print(a)
#     c=a+b
#     a=b
#     b=c
#     count+=1


# n=5
# a=0
# b=1
# count=1
# while count<=n:
#     print(a)
#     c=a+b
#     a=b
#     b=c
#     count+=1


#print the first 10 fibonacci sequence:
# n=10
# a=0
# b=1
# count=1
# while count<=n:
#     print(a)
#     c=a+b
#     a=b
#     b=c
#     count+=1


#print fibonacci number which are less than 50

# a=0
# b=1

# while a<=50:
#     print(a)
#     c=a+b
#     a=b
#     b=c

#check whether given number is present in fibonacci sequence or not
# n=int(input("Enter number :"))
# a=0
# b=1
# found=False
# while a<=n:
#     if(a==n):
#       found=True
    
    
#     c=a+b
#     a=b
#     b=c
# if(found):
#    print("present")
# else:
#    print("not present")
    




# INTERVIEW QUESTIONS - 1

#1.  Armstrong number
# n=153
# original=n
# total=0
# while n>0:
#     digit=n%10
#     n=n//10
#     total=total+digit**3
    
# if(total==original):
#     print("Armstrong")
# else:
#     print("not an armstrong number")


#2.Armstrong or not
# n=370
# original=n
# total=0
# while n>0:
#     digit=n%10
#     n=n//10
#     total+=digit**3
# if(total==original):
#     print("Armstrong Number")
# else:
#     print("not an armstrong number")
    


#3.4.check whether the number is present in fibonacci or not
# n=int(input("Enter Number:"))
# a=0
# b=1
# found=False
# while a<=n:
#     if(a==n):
#         found=True
#         break
#     c=a+b
#     a=b
#     b=c
# if(found):
#     print("present")

# else:
#     print("not present")



#5.check whether a number is both armstrong and fibonacci

# n=21

# original=n
# total=0
# fact=1
# while n>0:
#     digit=n%10
#     n=n//10
#     total+=digit**3
# if(total==original):
#     armstrong=True
# else:
#     armstrong=False

# a=0
# b=1
# while a<=n:
#     if(a==n):
#         found=True
#         break
#     c=a+b
#     a=b
#     b=c
# if(found):
#     fibonacci=True
# else:
#     fibonacci=False

# if(armstrong and fibonacci):
#     print("Number is both Armstrong and Fibonacci")
# elif(armstrong):
#     print("Number is Armstrong only")
# elif(fibonacci):
#     print("number is fibonacci only")
# else:
#     print("Neither of them")


#OR

# n = 21
# original = n

# # ARMSTRONG
# temp = n
# total = 0

# while temp > 0:
#     digit = temp % 10
#     temp = temp // 10
#     total += digit ** 3

# armstrong = (total == original)

# # FIBONACCI
# a = 0
# b = 1
# found = False

# while a <= n:
#     if a == n:
#         found = True
#         break
#     c = a + b
#     a = b
#     b = c

# fibonacci = found

# # FINAL
# if armstrong and fibonacci:
#     print("Both")
# elif armstrong:
#     print("Armstrong only")
# elif fibonacci:
#     print("Fibonacci only")
# else:
#     print("Neither")  


# INTERVIEW ROUND 2 (EASY - MEDIUM)

#1. armstrong or not:
# n=370
# original=n
# total=0
# while n>0:
#     digit=n%10
#     n=n//10
#     total+=digit**3
# if(total==original):
#     print("Armstrong")
# else:
#     print("armstrong kadh m kadh")


#2.first 8 fibonacci sequence:
# n=7
# a=0
# b=1
# count=0
# while count<=n:
#     print(a)
#     c=a+b
#     a=b
#     b=c
#     count+=1

#3.
# n=34
# found=False
# a=0
# b=1
# while a<=n:
#     if(a==n):
#         found=True
#         break
#     c=a+b
#     a=b
#     b=c
# if(found):
#     print("present")
# else:
#     print("not present")


#4.
# n=int(input("Enter the Number:"))

# original=n
# temp=n
# total=0
# while temp>0:
#     digit=temp%10
#     temp=temp//10
#     total+=digit**3
# if(total==original):
#     armstrong=True
# else:
#     armstrong=False

# a=0
# b=1
# while a<=n:
#     if(a==n):
#         found=True
#         break
#     c=a+b
#     a=b
#     b=c
# if(found):
#     fibonacci=True
# else:
#     fibonacci=False


# if(armstrong and fibonacci):
#     print("Both")
# elif(armstrong):
#     print("Armstrong only")
# elif(fibonacci):
#     print("Fibonacci only")
# else:
#     print("neither")

# #5.
# n=(153, 123, 370, 407, 500)
# original=n
# total=0
# count=0
# while n>0:
#     digit=n%10
#     n=n//10
#     total+=digit**3
#     count+=1

# if(total==original):
#     print("Armstrong")
# else:
#     print("not")



#1.
# n=371
# original=n
# total=0

# while n>0:
#     digit=n%10
#     n=n//10
#     total+=digit**3
# if(total==original):
#     print("It is an Armstrong Number")
# else:
#     print("It is not an Armstrong Number")

#2.
# n=55
# a=0
# b=1
# found=False
# while a<=n:
#     if(a==n):
#         found=True
#         break
#     c=a+b
#     a=b
#     b=c
# if(found):
#     print("It is present")
# else:
#     print("It is not present")


#3.
# a=0
# b=1
# while a<=200:
#     print(a)
#     c=a+b
#     a=b
#     b=c


#4.
# n=407

# original=n
# temp=n
# total=0
# while temp>0:
#     digit=temp%10
#     temp=temp//10
#     total+=digit**3
# if(total==original):
#     armstrong=True
# else:
#     armstrong=False

# a=0
# b=1
# found=False
# while a<=n:
#     if(a==n):
#         found=True
#         break
#     c=a+b
#     a=b
#     b=c
# if(found):
#     fibonacci=True
# else:
#     fibonacci=False

# if(armstrong and fibonacci):
#     print("both")
# elif(armstrong):
#     print("Armstrong only")
# elif(fibonacci):
#     print("Fibonacci only")
# else:
#     print("Neither")



#1.
# n=89

# original=n
# temp=n
# total=0
# while temp>0:
#     digit=temp%10
#     temp=temp//10
#     total+=digit**3
# if(total==original):
#     armstrong=True
# else:
#     armstrong=False

# a=0
# b=1
# found=False
# while a<=n:
#     if(a==n):
#         found=True
#         break
#     c=a+b
#     a=b
#     b=c
# if(found):
#     fibo=True
# else:
#     fibo=False

# if(armstrong and fibo):
#     print("both")
# elif(armstrong):
#     print("armstrong")
# elif(fibo):
#     print("fibo")
# else:
#     print("neither")



#2.
# a=0
# b=1
# while a<=100:
    
#     c=a+b
#     a=b
#     b=c
# print(a)


#3.
# n=500
# original=n
# total=0
# while n>0:
#     digit=n%10
#     n=n//10
#     total+=digit**3
# if(total==original):
#     print("Armstrong")
# else:
#     print("not armstrong")


#4.
# a=0
# b=1
# count=0
# while a<=100:
#     c=a+b
#     a=b
#     b=c
#     count+=1
# print(count)



#1.
a=0
b=1
total=0
while a<=50:
    total+=a
    c=a+b
    a=b
    b=c
print(total)



#2.largest fibonacci number less than 1000
a=0
b=1
while a<=1000:
    c=a+b
    a=b
    b=c
    print(a)



