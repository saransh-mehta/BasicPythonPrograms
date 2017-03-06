#palindrome string 2

a=input("enter the string : ")
p=len(a)-1
index=0
i=0
while(index<p):
    if(a[index]==a[p]):
        index=index+1
        p=p-1
    else:
        i=i+1
        break
    print("palindrome")
if i==1:
    print("not palindrome")
        
