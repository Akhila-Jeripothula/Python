# NESTED LOOPS *****


#1.
# i=1
# while i<=5:
#     j=1
#     while j<=i:
#         print("*",end="")
#         j+=1
#     print()
#     i+=1



#2.
# i=1
# while i<=5:
#     j=1
#     while j<=i:
#         print(j,end="")
#         j+=1
#     print()
#     i+=1


#3.
i=1
# while i<=5:
#     j=1
#     while j<=i:
#         print(i,end="")
#         j+=1
#     print()
#     i+=1



#4.
# i=4
# while i>=1:
#     j=1
#     while j<=i:
#         print("*",end="")
#         j+=1
#     print()
#     i-=1



#5.
# i=5
# while i>=1:
#     j=1
#     while j<=i:
#         print(j,end="")
#         j+=1
#     print()
#     i-=1



#6.
# i=1
# while i<=5:
#     j=5
#     while j>=i:
#         print(j,end="")
#         j-=1
#     print()
#     i+=1



#8.
# i=1
# while i<=5:
#     j=5
#     while j>=i:
#         print(i,end="")
#         j-=1
#     print()
#     i+=1


#9.
# i=1
# while i<=5:
#     j=i
#     while j>=1:
#         print(j,end="")
#         j-=1
#     print()
#     i+=1



#7.
#8.
# i=1
# while i<=5:
#     j=5
#     while j>=i:
#         print(i,end="")
#         j-=1
#     print()
#     i+=1


#9.
# i=1
# while i<=5:
#     j=5
#     while j>=6-i:
#         print(j,end="")
#         j-=1
#     print()
#     i+=1



#10.
# i=1
# while i<=5:
#     j=i
#     while j>=1:
#         print(j,end="")
#         j-=1
#     print()
#     i+=1




#***************************************


# 1.   

# 1
# 23
# 456
# 78910


#1.5 rows    2.j  3.j should increase
#code:
# num=1
# i=1
# while i<=5:
#     j=1
#     while j<=i:
        
#         j+=1
    
#     print()
#     i+=1
    



#2..
# i=5
# while i>=1:
#     j=1
#     while j<=i:
#         print(i,end="")
#         j+=1
#     print()
#     i-=1



#3.
# num=1
# i=5

# while i>=1:
#     j=1
#     while j<=i:
#         print(i,end="")
#         j+=1
#     print()
#     i-=1




# i=1
# count=0
# while i<=1800:
#     if(i%15==0 and i%8!=0):
#         count+=1
#     i+=1
# print(count)








# PHASE 1  -  INCREASING 


#LEVEL1 - EASYYY

#1. 

# *
# **
# ***
# ****
# *****

# i=1
# while i<=5:
#     j=1
#     while j<=i:
#         print("*",end="")
#         j+=1
#     print()
#     i+=1



#2.
# 1
# 12
# 123
# 1234
# 12345

# i=1
# while i<=5:
#     j=1
#     while j<=i:
#         print(j,end="")
#         j+=1
#     print()
#     i+=1



#3.

# 1
# 22
# 333
# 4444
# 55555

# i=1
# while i<=5:
#     j=1
#     while j<=i:
#         print(i,end="")
#         j+=1
#     print()
#     i+=1




#4.

# 12
# 123
# 1234
# 12345
# 123456

# i=1
# while i<=5:
#     j=1
#     while j<=i+1:
#         print(j,end="")
#         j+=1
#     print()
#     i+=1



#5.

# 2
# 23
# 234
# 2345
# 23456

# i=2
# while i<=6:
#     j=2
#     while j<=i:
#         print(j,end="")
#         j+=1
#     print()
#     i+=1

#  OR

# i=1
# while i<=5:
#     j=2
#     while j<=i+1:
#         print(j,end="")
#         j+=1
#     print()
#     i+=1



#6.

# 5
# 54
# 543
# 5432
# 54321

# i=1
# while i<=5:
#     j=5
#     while j>=6-i:
#         print(j,end="")
#         j-=1
#     print()
#     i+=1




#7.

# 9
# 98
# 987
# 9876
# 98765

# i=1
# while i<=5:
#     j=5
#     while j>=6-i:
#         print(j+4,end="")
#         j-=1
#     print()
#     i+=1


#  OR

# i=1
# while i<=5:
#     j=9
#     while j>=10-i:
#         print(j,end="")
#         j-=1
#     print()
#     i+=1



#8.

# 8
# 87
# 876
# 8765
# 87654


# i=1
# while i<=5:
#     j=8
#     while j>=9-i:
#         print(j,end="")
#         j-=1
#     print()
#     i+=1


#9.
# 3
# 34
# 345
# 3456
# 34567

# i=1
# while i<=5:
#     j=3
#     while j<=2+i:
#         print(j,end="")
#         j+=1
#     print()
#     i+=1



#10.
# 7
# 77
# 777
# 7777
# 77777


# i=1
# while i<=5:
#     j=1
#     while j<=i:
#         print("7",end="")
#         j+=1
#     print()
#     i+=1



#11.
# 12345
# 1234
# 123
# 12
# 1

# i=1
# while i<=5:
#     j=1
#     while j<=6-i:
#         print(j,end="")
#         j+=1
#     print()
#     i+=1


#12.

# *****
# ****
# ***
# **
# *


# i=1
# while i<=5:
#     j=1
#     while j<=6-i:
#         print("*",end="")
#         j+=1
#     print()
#     i+=1


#13.
# 1
# 21
# 321
# 4321
# 54321

# i=1
# while i<=5:
#     j=i
#     while j>=1:
#         print(j,end="")
#         j-=1
#     print()
#     i+=1


# Assessment:
#1.
# i=1
# while i<=5:
#     j=1
#     while j<=i:
#         print(j,end="")
#         j+=1
#     print()
#     i+=1

#2.
# i=1
# while i<=5:
#     j=2
#     while j<=i+1:
#         print(j,end="")
#         j+=1
#     print()
#     i+=1


#3.
# i=1
# while i<=5:
#     j=1
#     while j<=i:
#         print(5,end="")
#         j+=1
#     print()
#     i+=1


#4.
# i=1
# while i<=5:
#     j=3
#     while j<=2+i:
#         print(j,end="")
#         j+=1
#     print()
#     i+=1


#5.
# i=1
# while i<=5:
#     j=1
#     while j<=i:
#         print(9,end="")
#         j+=1
#     print()
#     i+=1


#6.
# i=1
# while i<=5:
#     j=1
#     while j<=4:
#         print(j*2,end="")
#         j+=1
#     print()
#     i+=1



#7.
# i=1
# while i<=5:
#     j=1
#     while j<=5:
#         print(j*2-1,end="")
#         j+=1
#     print()
#     i+=1


#8.
# i=1
# while i<=5:
#     j=1
#     while j<=5:
#         print(j+4,end="")
#         j+=1
#     print()
#     i+=1


#9.
# i=1
# while i<=5:
#     j=1
#     while j<=3:
#         print(i+2,end="")
#         j+=1
#     print()
#     i+=1


#10.
# i=1
# while i<=5:
#     j=1
#     while j<=4:
#         print(j+6,end="")
#         j+=1
#     print()
#     i+=1


11.
i=1
while i<=5:
    j=1
    while j<=i:
        print(2*j-1,end="")
        j+=1
    print()
    i+=1

#12.
# i=1
# while i<=5:
#     j=i
#     while j<=i*2:
#         print(2*j,end="")
#         j+=1
#     print()
#     i+=1


# 15.
# i=1
# while i<=5:
#     j=1
#     while j<=i:
#         print(j+10,end="")
#         j+=1
#     print()
#     i+=1


#13.
# i=1
# while i<=5:
#     j=1
#     while j<=i:
#         print(chr(65),end="")
#         j+=1
#     print()
#     i+=1
