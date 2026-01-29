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


#break and else:
# Python has a special feature: loop + else

# Rule:

# else runs only if the loop ends normally

# else does NOT run if break is executed

for i in range(1,10):
    if i==12:
        break
else:
    print("hcg")

#break cannot be used outside the loop(if it is used outside the loop it gives syntactic error)





#continuee