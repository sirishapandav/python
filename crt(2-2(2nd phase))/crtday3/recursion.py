def fun(n):
    if n==1:
        return 6
    fun(n-1)
    return fun(n-1)+n
res=fun(4)
print(res)