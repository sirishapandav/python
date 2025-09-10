#right angle triangle
n=5
for i in range(n):
    for j in range (i+1):
        print("*",end=" ")
    print()

#another method
n=5
for i in range(n):
    print("* "*(i+1))


#inverted triangle
n=5
for i in range(n-1,-1,-1):
    for j in range (i+1):
        print("*",end=" ")
    print()    

 #characters in right angle triangle
n=5
num=ord('A')
for i in range(n):
    for j in range (i+1):
        print(chr(65+j),end=" ")
    print()