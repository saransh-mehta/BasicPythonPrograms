# selection sort

lists=[]
n=int(input('Enter no. of elements'))
for i in range(0,n):
     a=input('Enter element :')
     lists.append(a)

def selectionSort(x):
    for i in range(0,n):
        minPos=i
        for j in range(i,n-1):
            if(x[j]>x[j+1]):
                minPos=j+1
        temp=x[i]
        x[i]=x[minPos]
        x[minPos]=temp
    print(x)
selectionSort(lists)
        
            
