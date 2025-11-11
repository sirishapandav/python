class Solution:
    def largestRectangleArea(self,heights:list[int])->int:
        st=[]
        ma=0
        for i,h in enumerate(heights):
            start=i
            while st and st[-1][1]>h:
                idx,height=st.pop()
                ma=max(ma,height*(i-idx))
                start=idx
            st.append((start,h))
        n=len(heights)
        for idx,height in st:
            ma=max(ma,height*(n-idx))
        return ma            
