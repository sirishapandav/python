#hollow pyramid
n=4
for i in range(n):
    for j in range(n-i-1):
        print(" ",end="")
    for k in range(2*i+1):
        if i==n-1 or k==0 or k==2*i:
            print("*",end="")
        else:
            print(" ",end="")
    print()