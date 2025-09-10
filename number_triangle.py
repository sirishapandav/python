#number triangle
n=5
for i in range(n):
    for j in range (i+1):
        print(j+1,end=" ")
    print()

#inverted triangle
n=5
for i in range(n-1,-1,-1):
    for j in range (i+1):
        print("*",end=" ")
    print()