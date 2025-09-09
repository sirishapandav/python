#decimal to binary
def dtob(n):
    res=""
    while (n!=0):
      rem=n%2
      if rem==1:
          res+="1"
      else:
          res+="0"
      n=n//2
    return res[::-1]
n=7
print(dtob(n))

#binary to decimal#
def btod(s):
    res=0
    p2=1
    for i in range(len(s)-1,-1,-1):
        if s[i]=="1":
            res+=p2
        p2=p2*2
    return res
s="101"
print(btod(s))