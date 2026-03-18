def longestOnes(nums,k):
    ml=0
    left=0
    z=0
    for r in range(len(nums)):
        if nums[r]==0:
            z+=1
        while z>k:
            if nums[left]==0:
                z-=1
            left+=1
        ml=max(ml,r-left+1)
    return ml                

nums=[1,0,1,0,1,0]
k=3
print(longestOnes(nums,k))