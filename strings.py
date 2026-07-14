#STRINS PROBLEMS

#1.print string charecters

# s="python"
# for ch in s:
#     print(ch)


#2.count charecters
# s="Akhila"
# count=0
# for ch in s:
#     count+=1
# print(count)


#3. count vowels
# s="Education"
# count=0
# for ch in s:
#     if ch.lower() in "a,e,i,o,u":
#      count+=1
# print(count)


#4. count consonants:
# s="Education"
# count=0
# for ch in s:
#     if ch.lower() not in "a,e,i,o,u":
#         count+=1
# print(count)


#5. count the digits in 
# s="abc1234"
# count=0
# for ch in s:
#     count+=1
# print(count)


#6.count the uppercase
# s="PyTHon"
# count=0
# for ch in s:
#     if ch.isupper():
#         count+=1
# print(count)


#7.reverse string:
# s="python"
# print(s[::-1])


#8. count frequency of charecters:

# s="banana"
# target="a"
# count=0
# for ch in s:
#     if ch==target:
#         count+=1
# print(count)



#9. check whether charecter exists or not
# s="python"
# found=False
# for ch in s:
#     if ch=="o":
#         found=True
# if(found==True):
#     print("charecter exists")
# else:
#     print("charecter not exists")



#10.count special charecters:
# s="abc@#12$"
# count=0
# for ch in s:
#     if ch not in ch.isalpha() and ch.isdigit() and ch==" ":
#         count+=1
# print(count)

#11.find the first uppercase:
# s="pythonIsFun"
# for ch in s:
#     if ch.isupper():
#         break
# print(ch)

#12.Find the first digit:
# s="abc123xyz"
# for ch in s:
#     if ch.isdigit():
#         break
# print(ch)



#PART 3 - STRING BUILDER

#1.reverse without slicing:
# s="python"
# new=""
# for ch in s:
#     new=ch+new
# print(new)


#2.remove spaces:
# s="Hello world"
# new=""
# for ch in s:
#     if ch!=" ":
#         new=new+ch
# print(new)


#3.replace every vowel with *
# d="python"
# new=""

# for ch in d:
#     if ch.lower() in "aeiou":
#         new=new+"*"
#     else:
#         new=new+ch
# print(new)

#4. Toggle
# s="AkHiLa"
# new=""
# for ch in s:
#     if ch.isupper():
#         new=new+ ch.lower()
#     elif ch.islower():
#         new=new+ch.upper()
# print(new)




#PART 4 - INTERVIEW PROBLEMS

#1.Palindrome
# s="python"
# new=""
# for ch in s:
#     new=ch+new
# if(s==new):
#     print("Palindrome")
# else:
#     print("Not a palindrome")


#OR 

s="madam"

if s==s[::-1]:
    print("Palindrome")
else:
    print("not palindrome")
