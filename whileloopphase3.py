# Phase 3 Topics
# 1.Armstrong Number
# 2.Strong Number
# 3.Perfect Number (revision)
# 4.Fibonacci sequence


#1.ARMSTRONG NUMBER:
n=407
original=n
total=0
while n>0:
    digit=n%10
    n=n//10
    total=total+digit**3
if(total==original):
    print("Armstrong number")
else:
    print("Not an Armstrong Number")


