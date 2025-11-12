class Node:
    def __init__(self,data):
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
    return head
def rev(head):
    curr=head
    prev=None
    while curr:
        nextN=curr.next
        curr.next=prev
        prev=curr
        curr=nextN
    return prev
def display(head):
    curr=head
    while curr:
        print(curr.data,end="->")
        curr=curr.next
    print("None")
arr=[1,2,3,4,5]    
head=createsl1(arr)
display(head)
rev1=rev(head)
display(rev1)