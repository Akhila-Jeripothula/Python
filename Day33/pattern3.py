#3.Inverted right triangle:

def inverted_triangle(n):
    for i in range(n, 0, -1):
        for j in range(i):
            print("*", end=" ")
        print()

inverted_triangle(4)

#output:

# * * * * 
# * * *
# * *
# *