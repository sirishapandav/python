class Solution:
    def countVowelSubstring(self,word: str) -> int:
        v='aeiou'
        c=0
        n=len(word)
        for i in range(n):
            if word[i]in v:
                u=set()
                for j in range(i,n):
                    if word[j] in v:
                        u.add(word[j])
                        if len==5:
                            c+=1
                    else:
                        break
        return c