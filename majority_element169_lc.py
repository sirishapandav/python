#O(logn)-TIME COMPLEXITY
def majorityelement(nums):
    nums.sort()
    return(nums[len(nums)//2])
nums=[1,1,2,2,2,2,1] 
print(majorityelement(nums))   


#O(1)-TIME COMPLEXITY
def majorityelement(nums):
    c=0
    v=0
    for num in nums:
        if c==0:
            v=num
        if num==v:
            c+=1
        else:
            c-=1
    return v            
nums=[1,1,2,2,2,2,1] 
print(majorityelement(nums))
