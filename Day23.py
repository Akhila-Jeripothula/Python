#break and continue statements

# break immediately exits the loop, even if the loop condition is still true.
for i in range(1,6):
    if i==3:
        break
    print(i)




i=1
while i<=6:
    if i==3:
        break 
    print(i)
    i+=1

#real life example of break statement
num=[1,2,4,6,8,9,77]
for i in num:
    if i==6:
        print("found")
        break