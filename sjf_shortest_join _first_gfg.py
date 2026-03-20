def sjf(bt):
    bt.sort()
    n=len(bt)
    wt=0
    tt=0
    for i in range(n):
        wt+=tt
        tt+=bt[i]
    return wt//n
bt=[4,1,3,2,7]
print(sjf(bt))    