def second_largest(nums):
    first = second = float('-inf')
    
    for num in nums:
        if num > first:
            second = first
            first = num
        elif num > second and num != first:
            second = num
            
    return second

print(second_largest([10, 20, 4, 45, 99]))

#output:
#46
#45
#21
