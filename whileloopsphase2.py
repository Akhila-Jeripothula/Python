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
# n=int(input("Enter number:"))
# i=1
# x=0
# y=0
# while i<=n:
#     if(n%i==0 ):
#         j=1
#         count=0
#         while j<=i:
#             if(i%j==0):
#                 count+=1
#             j+=1
#         if(count==2):
#             x+=i
#         else:
#             y+=i
#     i+=1
# print(x)
# print(y)
# print(x-y)


     

 





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


        

# #1.write a program to count the odd factors of a given number:
# # n=18
# # i=1
# # count=0
# # while i<=n:
# #     if(n%i==0 and i%2!=0):
# #         count+=1
# #     i+=1
# # print(count)


# #2.write a program to find product of all factors of a number:
# # n=6
# # i=1
# # product=1
# # while i<=n:
# #     if(n%i==0):
# #         product*=i
# #     i+=1
# # print(product)



# #3.check whether a number has exactly four factors:
# # n=int(input("Enter the number:"))
# # i=1
# # count=0
# # x=4
# # while i<=n:
# #     if(n%i==0):
# #         count+=1
# #     i+=1
# # if(count==x):
# #     print("yes")
# # else:
# #     print("no")


# #4.find the smallest factor of number excling 1
# # n=18
# # i=2
# # smallest=9
# # while i<=n:
# #     if(n%i==0 and smallest>i):
# #         smallest=i
# #     i+=1
# # print(smallest)


# 5.sum of perfect factors of a number:
# n=30
# i=1
# x=0
# while i<n:
#     if(n%i==0):
#         j=1
#         total=0
#         while j<i:
#             if(i%j==0):
#                 total+=j
#             j+=1
#         if(total==i):
#             x+=i
#     i+=1
# print(x)

 
# #6.check whether number is perfect ,prime ,strong
# n=int(input("Enter Number:  "))
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
#     if(n%i==0):
#         total+=i
#     i+=1
# if(total==n):
#     perfect=True
# else:
#     perfect=False
    
# original=n
# x=0
# while n>0:
#     digit=n%10
#     n=n//10
#     i=1
#     fact=1
#     while i<=digit:
#         fact*=i
#         i+=1
#     x+=fact
# if(x==original):
#     strong=True
# else:
#     strong=False

# if(prime and perfect and strong):
#     print("all")
# elif(prime):
#     print("prime")
# elif(perfect):
#     print("perfect")
# elif(strong):
#     print("strong")
# else:
#     print("neither")
    

#7.Largest prime factor of a number:
# n=int(input("enter number:"))
# i=1
# largest=0



# while i<=n:
#     if(n%i==0):

#         j=1
#         count=0
#         while j<=i:
#             if(i%j==0):
#                 count+=1
#             j+=1
#         if(count==2):
#             prime=True
#         else:
#             prime=False

        
#         if(count==2):
#             if(largest<i):
#                 largest=i
#     i+=1

# print(largest)



#Nested loops(i,j)

#1.count prime factors:
# n=30
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


#2.largest prime factor
# n=30
# i=1
# largest=0
# while i<=n:
#     if(n%i==0):
#         j=1
#         count=0
#         while j<=i:
#             if(i%j==0):
#                 count+=1
#             j+=1

#         if(count==2):
#             if(largest<i):
#                 largest=i
#     i+=1
# print(largest)



#3.sum of perfect dactor:
# n=30
# i=1
# total=0
# while i<n:
#     if(n%i==0):
#         j=1
#         x=0
#         while j<i:
#             if(i%j==0):
#                 x+=j
#             j+=1
#         if(x==i):
#             total+=i
#     i+=1
# print(total)


#4. prime,perfect,strong:
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
#     if(n%i==0):
#         total+=i
#     i+=1
# if(total==n):
#     perfect=True
# else:
#     perfect=False


# original=n
# total1=0
# while n>0:
#     digit=n%10
#     n=n//10
#     i=1
#     fact=1
#     while i<=digit:
#         fact*=i
#         i+=1
#     total1+=fact
# if(total1==original):
#     strong=True
# else:
#     strong=False

# if(prime and perfect and strong):
#     print("all")
# elif(prime):
#     print("prime")
# elif(perfect):
#     print("perfect")
# elif(strong):
#     print("strong")
# else:
#     print("neither")


#1.count composite number
# n=12
# i=1
# count=0
# while i<=n:
#     if(n%i==0):
        
#         j=1
#         x=0
#         while j<=i:
#             if(i%j==0):
#                 x+=1
#             j+=1
#         if(x!=2 and x!=1):
#             count+=1
#     i+=1
# print(count)

#2.sum of prime
# n=12
# i=1
# total=0
# while i<=n:
#     if(n%i==0):
#         j=1
#         x=0
#         while j<=i:
#             if(i%j==0):
#                 x+=1
#             j+=1
#         if(x==2):
#             total+=i
#     i+=1
# print(total)
    

#3.count strong digit
# n=123421
# count=0
# while n>0:
#     digit=n%10
#     n=n//10
#     i=1
#     fact=1
#     while i<=digit:
#         fact*=i
#         i+=1
#     if(fact==digit):
#         count+=1
# print(count)

#4.smallest prime factor
# n=84
# i=1
# smallest=9
# while i<=n:
#     if(n%i==0):
#         j=1
#         count=0
#         while j<=i:
#             if(i%j==0):
#                 count+=1
#             j+=1
#         if(count==2):
#             prime=True
#         else:
#             prime=False
#         if(count==2 and smallest>i):
#             smallest=i
#     i+=1
# print(smallest)


#5.Difference between sum of prime factors and sum of composite factors:
# n=12
# i=1
# x=0
# y=0
# while i<=n:
#     if(n%i==0):
#         j=1
#         count=0
#         while j>=i:
#             if(i%j==0):
#                 count+=1
#         if(count==2):
#             x+=i
#         elif(count>2):
#             y+=i
#     i+=1
# print(x-y)



#6.check whether all factors are prime or not
n=16
i=1
allprime=True
while i<=n:
    if(n%i==0):
        j=1
        count=0
        while j<=i:
            if(i%j==0):
                count+=1
            j+=1
        if(count!=2):
            allprime=False
    i+=1
print(allprime)





