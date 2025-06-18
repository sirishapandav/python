def maxSum(arr,k):
    n=len(arr)
    if n<=k:
        print("invalid")
        return -1
    window_sum=sum(arr[:k])
    max_sum=window_sum
    for i in range (n-k):
        window_sum=window_sum-arr[i]+arr[i+k]
        max_sum=max(window_sum,max_sum)
    return max_sum
#driver code
arr=[1,4,2,10,2,3,1,0,20]
k=4
print(maxSum(arr,k))