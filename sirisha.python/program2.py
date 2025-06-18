def special(nums,k):
    count=0
    n=len(nums)
    for i in range (n-2):
        if nums[i]+nums[i+2]==nums[i+1]:
           count+=1
    return count 
nums=[1,2,1,3,5]
k=3
print(special(nums,k))