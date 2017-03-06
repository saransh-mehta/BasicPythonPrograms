#count no of p in a string
a=str(input("enter the string : "))
count=0
for i in range(0,len(a)):
    if a[i]=='p':
        count=count+1
print("no. of times : ",count)
