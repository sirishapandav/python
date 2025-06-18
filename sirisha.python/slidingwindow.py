def window(nums,k):
    n=len(nums)
    maxi=0
    for i in range(n-k+1):
        window_sum=sum(nums[i:i+k])
        maxi=max(maxi,window_sum)   
    return maxi
nums=[1,2,6,2,4,1]
k=3
print(window(nums,k))