class Solution:
    def trap(self,height: list[int])->int:
        n=len(height)
        lm=rm=water=0
        l=0
        r=n-1
        while l<r:
            if height[1]<height[r]:
                water+=max(0,lm-height[1])
                lm=max(lm,height[1])
                l+=1
            else:
                water+=max(0,rm-height[r])
                rm=max(rm,height[r])
                r-=1
        return water            
height=[4,2,0,3,2,5]    