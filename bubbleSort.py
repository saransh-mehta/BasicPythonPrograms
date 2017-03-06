#bubble sort
lists=[]
n=int(input('Enter no. of elements'))
for i in range(0,n):
     a=int(input('Enter element :'))
     lists.append(a)
def bubbleSort(x):
    print(x)
    for i in range(0,n):
        for j in range(0,n-1-i):
            if(x[j]>x[j+1]):
                temp=x[j]
                x[j]=x[j+1]
                x[j+1]=temp
                print(x)
bubbleSort(lists)
                
            
    
