#left shift#
def checkith(n,i):
    if (n&(1<<i))!=0:
        return 1
    else:
        return 0
n=5
i=2
print(checkith(n,i))

#right shift#
def checkithbit(n,i):
    if((n>>i)&1==0):
        return False
    return True
n=5
i=2
print(checkithbit(n,i))

#set ith bit#
def setithbit(n,i):
    return(n|(1<<i))
n=5
i=2
print(setithbit(n,i))

#clear ith bit#
def clearithbit(n,i):
    return(n&~(1<<i))
n=5
i=2
print(clearithbit(n,i))


#toggle#
def toggle(n,i):
    return(n^(1<<i))
n=5
i=2
print(toggle(n,i))

#count no.of set bits#
n=5
c=0
while(n!=0):
    rem=n%2
    if rem==1:
        c+=1
    n=n//2
print(c)  

#in bit manipulation
n=5
c=0
while(n!=0):
    n=n&(n-1)
    c+=1
    print(c)