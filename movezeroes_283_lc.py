#class solution:
def movezeroes(self,nums: list[int])->None:
        idx=0
        for num in nums:
            if num!=0:
                nums[idx]=num
                idx+=1
        for i in range(idx,len(nums)):
            nums[i]=0        
        return nums
nums=[0,1,0,3,12]
print(movezeroes(nums))