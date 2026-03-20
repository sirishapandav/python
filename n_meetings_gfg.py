#n meetings in one room#
def maximumMeetings(self,start,end):
    meetings=[]
    n=len(start)
    for i in range(n):
        meetings.append((end[i],start[i]))
    meetings.sort()
    le=-1
    cnt=0
    for e,s in meetings:
        if s>le:
            cnt+=1
            le=e
    return cnt            