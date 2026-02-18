#4.Number increasing triangle:
def number_triangle(n):
    for i in range(1, n+1):
        for j in range(1, i+1):
            print(j, end=" ")
        print()

number_triangle(4)

#output:


# 1 
# 1 2
# 1 2 3
# 1 2 3 4