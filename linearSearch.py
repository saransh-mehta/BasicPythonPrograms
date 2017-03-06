#linear search

def linearSearch(a,x):
    flag=0

    for i in range(0,len(a)-1):
        if(a[i]==x):
            print('element found at',i+1)
            flag=1
            break
        
    if (flag==0):
        print('element not in list')
