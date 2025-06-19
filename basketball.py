def max_subarray_score(n,k,a):
    max_score=0
    for i in range(n-k+1):
        score=0
        for j in range(k):
            position=i+j+1
            score+=position*a[i+j]
        max_score=max(max_score, score)
    return max_score
n=int(input())
k=int(input())
a=list(map(int, input().split()))
print(max_subarray_score(n,k,a))