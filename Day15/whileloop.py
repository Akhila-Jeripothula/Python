#Python majorly have 2 loops(while and for)

#While Loop(Repeats the code as long as the condition is true)

# 1.print numbers 1 to 5
i=1
while i<=5:
    print(i)
    i+=1

# 2.print even numbers
i=0
while i<=10:
    print(i)
    i+=2

# 3. decreasing numbers
count = 5
while count > 0:
    print(count)
    count -= 1



#user input 
password = ""
while password != "python":
    password = input("Enter password: ")
print("Access granted")


# #infinite loop
# while True:
#     print("Hello")



#using break in loop
i = 1

while i <= 10:
    if i == 6:
        break
    print(i)
    i += 1


#using continue in loop
i = 0

while i < 5:
    i += 1
    if i == 3:
        continue
    print(i)



