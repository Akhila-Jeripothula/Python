#1. converting while loops to for loop

#1.
# for i in range(1,11):
#     print(i)

# #2.
# for i in range(2,20,2):
#     print(i)

#3.
# for i in range(9,0,-1):
#     print(i)

#4.
# for i in range(10,1,-2):
#     print(i)




#find char

# str="Akhila Jeripothula"
# for char in str:
#     if(char=="o"):
#         print("found")
#         break
#     print(char)
# else:
#     print("end")



#traverse the elements
nums=[1,4,9,16,25,36,49,64,81,100]
x=49
idx=0
for num in nums:
    if(num==x):
        print("found at idx",idx)
        break
    idx+=1


# nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# x = 49
# idx = 0

# for num in nums:
#     if num == x:
#         print(f"found at idx {idx}")
#         break
#     idx += 1