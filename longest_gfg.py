#longest substring with k units#
#geeks for geeks#
class Solution:
    def longestKSubstr(self,s,k):
        freq={}
        left=0
        l=-1
        for r in range(len(s)):
            if s[r] in freq:
                freq[s[r]]+=1
            else:
                freq[s[r]]=1
            while len (freq)>k:
                freq[s[left]]-=1
                if freq[s[left]]==0:
                    del freq[s[left]]
                left+=1
            if len(freq)==k:
                l=max(l,r-left+1)
        return 1
                       