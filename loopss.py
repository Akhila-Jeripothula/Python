#LOOPS

#WHILE LOOP




#PHASE 1- NUMBER DIGITS

# count=0
# while count<=5:
#     print("Akshaya is full of Attitude")
#     count=count+1
#     print(count)


# i=1
# while i<=10:
    
#     print(i)
#     i+=1


# x=10
# while x>=1:
#     print(x)
#     x-=1


#print numbers from 1 to 100
# i=0
# while i<=100:
#     print(i)
#     i+=1

#print numbers 100 to 1
# i=100
# while i>=1:
#     print(i)
#     i-=1

#print multiplication table:
# n=int(input("Enter the number"))
# i=1
# while i<=10:
#     print(n*i)
#     i+=1





# n=["Akshaya","Akhila","Funny","Pranav","Vikhyat"]
# i=0
# while i<len(n):
#     print(n[i])
#     i+=1


#finding number from a tuple


#BREAK:used to terminate the loop when encountered
#CONTINUE:terminates execution in current iteration and continues the execution of the loop with the next iteration.


#break:
# nums=(2,3,4,5,6,7,8,9)
# x=6
# i=0
# while i<len(nums):
#     if(nums[i]==x):
#         print("Number found at",i)
#         break
#     else:
#         print("Finding")
#     i+=1
# print("end of loop")


#CONTINUE

# i=0
# while i<=15:
#     if(i%2==0):
#         i+=1
#         continue
#     print(i)
#     i+=1


# sum of first 5 numbers

# n=5
# i=1
# total=0
# while i<=n:
#     total+=i
#     i+=1
# print(total)


#count of digits:

# n=12345
# count=0
# while n>0:
#     n=n//10
#     count+=1

# print(count)



#reverse of a number

# n=34567
# x=0
# while n>0:
#     y=n%10
#     x=x*10+y
#     n=n//10
# print(x)



#palindrome

# n=int(input("Enter the number:"))
# original = n
# reverse = 0
# while n>0:
#     digit = n%10
#     reverse=reverse*10+digit
#     n=n//10
# if(original==reverse):
#     print("The given number is palindrome")
# else:
#     print("The given number is not a palindrome")
    



#sum of digits

# n=9876
# i=1
# total=0
# while i<=n:
#     n=n//10
#     total+=i
#     i+=1
# print(total)


# n=1221
# original=n
# reverse=0
# while n>0:
#     digit=n%10
#     reverse=reverse*10+digit
#     n=n//10
# if(original==reverse):
#     print("Palindrome")
# else:
#     print("Not a palindrome")




#reverse:
# n=5070
# reverse=0
# while n>0:
#     digit=n%10
#     reverse=reverse*10+digit
#     n=n//10
# print(reverse)


#sum of digits


# n=9876

# total=0
# while n>0:
#     digit=n%10
#     n=n//10
#     total+=digit
    
# print(total)



#product of digits

# n=234
# product=1
# while n>0:
#     digit=n%10
#     n=n//10
#     product*=digit
# print(product)



#largest number:
# n=58372
# largest=0
# while n>0:
#      digit=n%10
#      n=n//10
#      if(digit>largest):
#           largest = digit
# print(largest)


#smallest

# n=58372
# smallest=8
# while n>0:
#     digit=n%10
#     n=n//10
#     if(digit<smallest):
#         smallest=digit
# print(smallest)



#print the count of even digits
# n=123456
# count=0
# while n>0:
#     digit=n%10
#     n=n//10
#     if(digit%2==0):
#         count+=1
# print(count)

#count of odd digtd
# n=1234567
# count=0
# while n>0:
#     digit=n%10
#     n=n//10
#     if(digit%2!=0):
#         count+=1
# print(count)


#sum of even digits


# n=1234567
# total=0
# count=0
# while n>0:
#     digit=n%10
#     n=n//10
#     if(digit%2!=0):
#         count+=1
#         total+=digit
# print(total)


#Questionsss

#1.count zero digits

# n=10203040
# count=0
# while n>0:
#     digit=n%10
#     n=n//10
#     if(digit==0):
#         count+=1
# print(count)



#2. sum of digits greater than 5

# n=987654
# total=0
# while n>0:
#     digit=n%10
#     n=n//10
#     if(digit>5):
#         total+=digit
# print(total)


#3.count digits divisible by 3
# n=123456789
# count=0
# while n>0:
#     digit=n%10
#     n=n//10
#     if(digit%3==0):
#         count+=1
# print(count)


#4.second largest
# n=58372
# largest=0
# secondlargest=0
# while n>0:
#     digit=n%10
#     n=n//10
#     if(largest<digit):
#         secondlargest=largest
#         largest=digit
#     elif(secondlargest<digit):
#         secondlargest=digit
# print(secondlargest)



#5.
# n=1234567
# product=1
# while n>0:
#     digit=n%10
#     n=n//10
#     if(digit%2!=0):
#         product*=digit
# print(product)


#6
# n=2468
# all_even=True
# while n>0:
#     digit=n%10
#     n=n//10
#     if(digit%2!=5):
#         all_even=False
# print(all_even)


#5 there or not
# n=123456
# found=False
# while n>0:
#     digit=n%10
#     n=n//10
#     if(digit==5):
#         found=True
# if(found):
#     print("found")
# else:
#     print("not found")





#difference between sum of even digits and odd digits

# n=123456
# x=0
# y=0
# while n>0:
#     digit=n%10
#     n=n//10
#     if(digit%2==0):
#         x+=digit
#     if(digit%2!=0):
#         y+=digit
# print(x)
# print(y)
# print(x-y)


#5
# n=1234567
# found=False
# while n>0:
#     digit=n%10
#     n=n//10
#     if(digit==5):
#         found=True
# if found:
#     print("found")
# else:
#     print("not found")



#frequency of particular digit
# n=122233344444
# count=0
# x=4
# while n>0:
#     digit=n%10
#     n=n//10
#     if(digit==x):
#         count+=1
# print(count)



# 1.count digits
# 2.sum of digits
# 3.product of digits
# 4.reverse
# 5.palindrome
# 6.largest 
# 7.smallest
# 8.count even digits
# 9.count odd digits
# 10.sum of even digits
# 11.sum of odd digits
# 12.count zero digits
# 13.sum of digits greater than 5
# 14.count digits divisible by 3
# 15.second largest
# 16.product of odd digits
# 17.check all are even or not
# 18.difference betweensum of even and odd digits
# 19.check whether number contains 5
# 20.frequenct of particlular digit





#MOCK INTERVIEW

#1.Count digits greater than 7
# n = 8723498
# count=0
# while n>0:
#     digit=n%10
#     n=n//10
#     if(digit>7):
#         count+=1
# print(count)

#2.sum of even digits
# n = 123456
# total=0
# while n>0:
#     digit=n%10
#     n=n//10
#     if(digit%2==0):
#         total+=digit
# print(total)

#3.check if number contains number of zero
# n = 90712
# found=False
# while n>0:
#     digit=n%10
#     n=n//10
#     if(digit==0):
#         found=True
# if found:
#     print("found")
# else:
#     print("not found")


#4.revrse
# n = 12050
# reverse=0
# while n>0:
#     digit=n%10
#     n=n//10
#     reverse=reverse*10+digit
# print(reverse)



#5.product of digits greater than 3
# n = 1234567
# product=1
# while n>0:
#     digit=n%10
#     n=n//10
#     if(digit>3):
#         product*=digit
# print(product)


# 6. count digits divisible by 2 or 3
# n=123456789
# count=0
# while n>0:
#     digit=n%10
#     n=n//10
#     if(digit%2==0 or digit%3==0):
#          count+=1
# print(count)


# #7.second largest digit
# n = 907352
# largest=0
# secondlargest=0
# while n>0:
#     digit=n%10
#     n=n//10
#     if(digit>largest):
#         secondlargest=largest
#         largest=digit
#     elif(digit>secondlargest and digit!=largest):
#         secondlargest=digit
# print(secondlargest)



#ROUND 3-INTERVIEW


#1.Count digits that are BOTH even AND greater than 3

# n = 5837264
# count=0
# while n>0:
#     digit=n%10
#     n=n//10
#     if(digit%2==0 and digit>3):
#         count+=1
# print(count)


#2.Check if number contains BOTH 3 and 7

# n = 1234756
# found3=False
# found7=False
# while n>0:
#     digit=n%10
#     n=n//10
#     if(digit==3 ):
#         found3=True
#     elif(digit==7):
#         found7=True
# if found3 and found7:
#     print("yes")
# else:
#     print("no")


#3.Sum digits at odd positions (right to left), but only if digit is odd

# n = 987654
# odd_sum=0
# pos=1
# while n>0:
#     digit=n%10
#     n=n//10
#     if(pos%2!=0  and  digit%2!=0):
#         odd_sum+=digit
#     pos+=1
# print(odd_sum)



#4.Find the SECOND largest EVEN digit

# n = 9078624
# largest=0
# secondlargest=0
# while n>0:
#     digit=n%10
#     n=n//10
#     if digit%2==0:

#       if(digit>largest):
#         secondlargest=largest
#         largest=digit
#       if(digit>secondlargest):
#         secondlargest=digit

# print(secondlargest)


#5.Difference between: sum of digits divisible by 3 and sum of digits NOT divisible by 3

# n = 123456789
# x=0
# y=0
# while n>0:
#     digit=n%10
#     n=n//10
#     if(digit%3==0):
#         x+=digit
#     elif(digit%3!=0):
#         y+=digit
# print(x)
# print(y)
# print(x-y)




#1.
# n=583726
# count=0
# while n>0:
#     digit=n%10
#     n=n//10
#     if(digit>5):
#         count+=1
# print(count)


#2.
# n=1234567
# total=0
# while n>0:
#     digit=n%10
#     n=n//10
#     if(digit%2!=0):
#         total+=digit
# print(total)


#3.
# n=1234056
# count=0
# while n>0:
#     digit=n%10
#     n=n//10
#     if(digit==0):
#         count+=1
# if(count>=0):
#     print("contains")
# else:
#     print("Does not contain")


#4.
# n=123456789
# count=0
# while n>0:
#     digit=n%10
#     n=n//10
#     if(digit%2==0 and digit%3==0):
#         count+=1
# print(count)


#5.
# n=583729
# largest=0
# secondlargest=0
# while n>0:
#     digit=n%10
#     n=n//10
#     if(digit>largest):
        
#         secondlargest=largest
#         largest=digit
#     elif(digit>secondlargest and digit!=largest):
#         secondlargest=digit
# print(secondlargest)


#6.
n=12345
x=0
y=0
pos=1

while n>0:
    digit=n%10
    n=n//10
    
    if(pos%2!=0):
        y+=digit
    else:
        x+=digit

    pos+=1
print(y-x)
