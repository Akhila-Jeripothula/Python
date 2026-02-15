#LEETCODE:

#1.Two Sum problem

#brute force:
# def twosum(nums,target):
#     for i in range(len(nums)):
#         for j in range(i+1,len(nums)):
#             if nums[i]+nums[j]==target:
#                 return [i,j]
# nums=[1,2,3]
# target=5
# result=twosum(nums,target)
# print(result)

#dictionary
def twoSum(nums, target):
    seen = {}   # dictionary to store number and its index
    
    for i in range(len(nums)):
        needed = target - nums[i]
        
        if needed in seen:
            return [seen[needed], i]
        
        seen[nums[i]] = i
nums=[1,2,3]
target=3
result=twosum(nums,target)
print(result)


#functions:
