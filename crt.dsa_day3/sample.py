class Node:
    def __init__(self,data):
        self.data=data
        self.data=data
        self.next=None
def createsl1(arr):
    head=None
    for data in arr:
        if head is None:
            head=Node(data)
            curr=head
        else:
            curr.next=Node(data)
            curr=curr.next
class LL:
    def midd(self):
        while  curr:
            c+=1
            curr=curr.next
        mid=c//2
        curr=head
        for i in range(mid):
            curr=curr.next
        return curr     
ll=LL()
ll.creates11([1,2,3,4,5])
kk=ll.midd()
print(kk.data)       