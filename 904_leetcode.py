class solution:
    def totalFriut(self,friuts:list[int])->int:
        freq={}
        left=0
        ans=0
        for r in range(len(friuts)):
            if friuts[r]in freq:
                freq[friuts[r]]+=1
            else:
                freq(friuts[r])=1
            while len(freq)>2:
               freq[friuts[left]]-=1
               if freq[friuts[left]]==0:
                   del freq[friuts[left]]
               left+=1
            ans=max(ans,r-left+1)
        return ans                  
