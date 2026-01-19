# for loop with string

#1.
for i in "Akhila":
    print(i)

    # output
    # A
    # K
    # h 
    # i 
    # l 
    # a 

# 2. for loop 

consistency=["Navya","Kerthi","Ashritha","Akhila","pavani","Keerthi"]#list(o,c,d)
for i in consistency:
    print(i)

consistency=("Navya","Kerthi","Ashritha","Akhila","pavani","Keerthi")#tuple(o,d)
for i in consistency:
    print(i)

consistency={"name":"Akhila","age":20} #dict(o,c)
for key,value in consistency.items():
    print(key,value)