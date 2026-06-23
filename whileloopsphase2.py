#PHASE 2: FACTORS AND FACTORIAL

#general while loop:
# n=5
# i=1
# while i<=n:
#     print(i)
#     i+=1



#Factorial:

# n=int(input("Enter the number:"))
# i=1
# fact=1
# while i<=n:
#     fact*=i
#     i+=1
# print(fact)


#factorial of 20
# n=20
# i=1
# fact=1
# while i<=n:
#     fact*=i
#     i+=1
# print(fact)







#FACTORS:

# 1.
# n=12
# i=1
# while i<=n:
#     if(n%i==0):
#         print(i)
#     i+=1


#2. count of factors of 18
# n=18
# i=1
# count=0
# while i<=n:
#     if(n%i==0):
#         count+=1
        
#     i+=1
# print(count)


#3.sum of factors of a number
# n=12
# i=1
# total=0
# while i<=n:
#     if(n%i==0):
#         total+=i
#     i+=1
# print(total)




# PRIME OR NOT

#1.
# n=13
# i=1
# count=0
# while i<=n:
#     if(n%i==0):
#         count+=1
#     i+=1
# if(count==2):
#     print("Prime")
# else:
#     print("not prime")
   
#2.
# n=15
# i=1
# count=0
# while i<=n:
#     if(n%i==0):
#         count+=1
#     i+=1
# if(count==2):
#     print("Prime")
# else:
#     print("Not Prime")    

# n=1
# i=1
# count=0
# while i<=n:
#     if(n%i==0):
#         count+=1
#     i+=1
# if(count==2):
#     print("prime")
# else:
#     print("not prime")




# PERFECT NUMBER
# n=int(input("Enter the number:"))
# i=1
# total=0
# while i<n:
#     if(n%i==0):
#         total+=i
#     i+=1
# if(total==n):
#     print("perfect number")
# else:
#     print("not a perfect number")




#interview questions:
#1.
# n=5
# i=1
# fact=1
# while i<=n:
#     fact*=i
#     i+=1
# print(fact)

#2.
# n=20
# i=1
# count=0
# while i<=n:
#     if(n%i==0):
#        count+=1
#     i+=1
# print(count)
 

#3.
# n=10
# i=1
# total=0
# while i<=n:
#     if(n%i==0):
#         total+=i
#     i+=1
# print(total)



#4.
# n=12
# i=1
# count=0
# while i<=n:
#     if(n%i==0 and i%2==0):
#         count+=1
#     i+=1
# print(count)



#5.
# n=18
# i=1
# total=0
# while i<=n:
#     if(n%i==0 and i%2!=0):
#         total+=i
#     i+=1
# print(total)


#6.
# n=20
# i=1
# largest=0
# while i<n:
#     if(n%i==0 and i>largest):
#         largest=i
#     i+=1
# print(largest)


#7.
# n=int(input("Enter the number:"))

# i=1
# count=0
# while i<=n:
#     if(n%i==0):
#         count+=1
#     i+=1
# if(count==2):
#     prime=True
# else:
#     prime=False

# i=1
# total=0
# while i<n:
#         if(n%i==0):
#             total+=i
#         i+=1
# if(total==n):
#     perfect=True
# else:
#     perfect=False

# if(prime and perfect):
#      print("both prime and perfect")
# elif(prime):
#      print("prime only")
# elif(perfect):
#      print("perfect only")
# else:
#      print("neither prime nor perfect")



#8.
# n=12
# i=1
# x=0
# y=0
# while i<=n:
#     if(n%i==0 and i%2==0):
#           x+=i
#     if(n%i==0 and i%2!=0):
#           y+=i
#     i+=1
# print(x-y)
          
  
#9.
# n=int(input("Enter Number:"))
# i=1
# count=0
# while i<=n:
#     if(n%i==0):
#         count+=1
#     i+=1
# if(count>4):
#     print("yes")
# else:
#     print("no")




#10.because it doesnot have any factors.it does not follow the rules of prime and perfect numbers


#11.count prime factors:
# n=12
# i=1
# count=0
# while i<=n:
#     if(n%i==0):
#         j=1
#         count1=0
#         while j<=i:
#             if(i%j==0):
#                 count1+=1
#             j+=1
#         if(count1==2):
#             count+=1
#     i+=1
# print(count)









#12.largest odd factor
# n=36
# i=1
# largest=0
# while i<=n:
#     if(n%i==0 and i%2!=0 and i>largest):
#         largest=i
#     i+=1
# print(largest)


#13. check whether all factors are even:
# n=int(input("Enter Number : "))
# i=1
# alleven=True
# while i<=n:
#     if(n%i==0 and i%2!=0):
#         alleven=False

#     i+=1
# if(alleven):
#     print("All are even")
# else:
#     print("not all are even")



#14. Difference between sum of prime factors and sum of non prime factors
n=int(input("Enter number:"))
i=1
x=0
y=0
while i<=n:
    if(n%i==0 ):
        j=1
        count=0
        while j<=i:
            if(i%j==0):
                count+=1
            j+=1
        if(count==2):
            x+=i
        else:
            y+=i
    i+=1
print(x)
print(y)
print(x-y)


     

 





#15.
# n=145
# original=n
# total=0
# while n>0:
#     digit=n%10
#     i=1
#     fact=1

#     while i<=digit:
#         fact*=i
#         i+=1
#     total+=fact

#     n=n//10
# if (total==original):
#     print("strong number")
# else:
#     print("not a strong number")


        



