#x in square
n=7
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==0 or j==n-1:
            print("*",end=" ")
        elif(i==j) or j==n-i-1:
            print("*",end=" ")   
        else:
            print(" ",end=" ")
    print()