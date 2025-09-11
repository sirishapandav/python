def min2(arr):
    min1=max1=arr[0]
    for num in arr:
        if num<min1:
            min1=num
        if num>max1:
            max1=num
    min2=float('inf')
    max2=float('-inf')
    for num in arr:
        if min1<num<min2:
            min2=num
        if max1>num>max2:
            max2=num
    if min1==max1:
        print("all are same")
        return
    if min==float('inf'):
        print("no 2nd min")
    else:          
        print(min2)
    if max2==float('-inf'):
        print("no 2nd max")
    else:
        print(max2)
arr=[7,5,3,1,9]
min2(arr)                 