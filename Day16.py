# While Loop
#while loop is used to repeat the code till the condition is true

#syntax: while(condition):
           
# 1                              
i=3                                  
while(i<=9):                        
    print("Akhila")
    i+=1

    # i=3
    while(i<=9):
        print(i)  error because it is infinite loop



# 2. while loop with user input
# password=""

# while password!= "python":
#     password=input("Enter your password")
# print("Access granted")


# 3. while loop using break statement
i = 1
while i <= 10:
    if i == 5:
        break
    print(i)
    i += 1


# 4. while loop with continue statement(skips the current loop)
i=1
while(i<=10):
    i+=1
    if i==5:
        continue
    print(i)


# 5. while loop with else(only when loop ends normally without break)
i=3
while(i<=7):
    i+=1
    print(i)
else:
    print("executed successfully")


# 6.Nested while Loop(loop inside loop)
i = 1
while i <= 3:
    j = 1
    while j <= 2:
        print(i, j)
        j += 1
    i += 1



#7. while loop pattern
i=1
while(i<=7):
    print("*"*i)
    i+=1

#8.










