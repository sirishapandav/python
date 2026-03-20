class Solution:
    def canJump(self, nums: list[int]) -> bool:
        n=len(nums)
        maxi=0
        for i in range(n):
            if i>maxi:
                return False
            else:
                maxi=max(maxi,i+nums[i])
        return True        