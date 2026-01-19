#for-break and continue

#1.break(stops)
for i in range(1,8):
    if i==5:
        break
    print(i)
    # 1
    # 2
    # 3
    # 4

#2.continue(skips current iteration)
for i in range(1,8):
    if i==5:
        continue
    print(i)
    # 1
    # 2
    # 3
    # 4
    # 6
    # 7

