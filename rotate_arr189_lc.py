class solution:
    def rotate(self,nums: list[int],k:int)->None:
        n=len(nums)
        k=k%n
        nums[:]=nums[-k:]+nums[:-k]


  #another method
n=len(nums)
k=k%n
def reve(l,r):
    while l<r:
        nums[1],nums[r]=nums[r]
        l+=1
        r-=1
reve(0,n-1)
reve(0,k-1)        
reve(k,n-1)