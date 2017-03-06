#binary Search
import bisect

def binarySearch():

    lists=[]

    n=int(input('Enter no. of elements'))
    for i in range(0,n):
        a=int(input('Enter element :'))
       
        bisect.insort(lists,a)
    ele=int(input('Enter the element to be searched'))

    #binary search
    end=len(lists)
    start=0
    flag=0
    while (start<end):
        mid=int((start+end)/2)
        if(ele==lists[mid]):
            print('element at',mid)
            flag=1
            break
        if(ele<lists[mid]):
            end=mid-1
        if(ele>lists[mid]):
            start=mid+1
    if(flag==0):
        print('element not in list')
binarySearch()
        
        
