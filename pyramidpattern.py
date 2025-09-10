#pyramid
n=4
for i in range(n):
    print(" "*(n-i-1)+("* ")*(i+1))

#another method
n=4
for i in range(n):
    for j in range(n-i-1):
        print(" ",end="")
    for j in range(i+1):
        print("* ",end="")
    print()       

#pyramid odd numbers
n=5
for i in range(n):
    for j in range(n-i-1):
        print(" ",end=" ")
    for j in range(2*i+1):
        print("* ",end="")
    print()     
