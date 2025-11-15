def bs(arr,x):
    l,r=0,len(arr)
    while l<r:
        mid=(l+r)//2
        if arr[mid]<+x:
            l=mid+1
        else:
            r=mid
    return l
arr=[1,2,3,4,5,6,7]
x=4
print(bs(arr,x))