#brute force#
class Solution:
    def characterReplacement(self,s: str,k:int)->int:
        n=len(s)
        ans=0
        for i in range(n):
            freq=[0]*26
            mf=0
            for j in range(i,n):
                idx=ord(s[j])-ord('A')
                freq[idx]+=1
                mf=max(mf,freq[idx])
                if(j-i+1)-mf<=k:
                    ans=max(ans,j-i+1)
        return ans  
    

#sliding window technique#
class Solution:
    def characterReplacement(self,s: str,k:int)->int:
        n=len(s)
        left=0
        freq={}
        mf=0
        ans=0
        for r in range(n):
            if s[r] in freq:
                freq[s[r]]+=1
            else:
                freq[s[r]]=1
            mf=max(mf,freq[s[r]])
            while(r-left+1)-mf>k:
                freq[s[left]]-+1
                left+=1
            ans=max(ans,r-left+1)
        return ans                

