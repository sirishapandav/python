'''brute force'''
class solution:
    def maxscore(self, cardPoints:list[int],k:int):
        ms=0
        n=len(cardPoints)
        for i in range(k+1):
            s=0
            for left in range(i):
                s+=cardPoints[left]
            for r in range(k-i):
               s+=cardPoints[n-1-r]
            ms=max(ms,s)
        return ms

    arr=[1,7,3,8,9,3]
    k=1
    print()
                


 #sliding window#

def maxscore(cardPoints,k):
    n=len(cardPoints)
    wsize=n-k
    ws=sum(cardPoints[:wsize])
    mws=ws
    total=sum(cardPoints)
    for i in range(wsize,n):
        ws+=cardPoints[i]-cardPoints[i-wsize]
        mws=min(mws,ws)
    return total-mws 
cardPoints=[1,4,3,2]
k=1
print(maxscore(cardPoints,k))                    