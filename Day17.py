# practising while loop with patterns
# 1.

i=7
while i>=1:
    print("*"*i)
    i-=1


# *******
# ******
# *****
# ****
# ***
# **
# *




# 2.
i=1
while(i<=7):
    print(str(i)*i)
    i+=1

# 1
# 22
# 333
# 4444
# 55555
# 666666
# 7777777





# 3.
i=1
while(i<=5):
    print("*"*5)
    i+=1
#output:
# *****
# *****
# *****
# *****
# *****

#4.
i=1
while(i<=5):
    print(i*i)
    i+=1

#output:
# 1
# 4
# 9
# 16
# 25


#5.sum of numbers
sum = 0
for i in range(1, 11):
    sum += i
print(sum)
#output-55

#6.Largest number
nums = [10, 45, 2, 90, 33]
largest = nums[0]

for n in nums:
    if n > largest:
        largest = n

print(largest)
#output:90
