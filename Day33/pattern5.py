#5.Same number triangle:
def same_number_triangle(n):
    for i in range(1, n+1):
        for j in range(i):
            print(i, end=" ")
        print()

same_number_triangle(4)

#output:
# 1 
# 2 2
# 3 3 3
# 4 4 4 4