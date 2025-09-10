#floyls triangle    
n=4
num=1
for i in range(n):
    for j in range(i+1):
        print(num,end=" ")
        num=num+1
    print()

#characters in floyls triangle
n=4
num=ord('A')
for i in range(n):
    for j in range(i+1):
        print(chr(num),end=" ")
        num=num+1
    print()