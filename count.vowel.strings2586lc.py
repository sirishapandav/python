class solution:
    def vowelstrings(self,words:list[str],left,right):
        v='aeiou'
        c=0
        for i in range(left,right+1):
            w=words[i]
            if w[0] in v and w[-1] in v:
                c+=1
        return c        
