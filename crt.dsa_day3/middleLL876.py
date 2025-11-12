class Solution:
    def middleNode(self,head:Optional[ListNode])->Optional[Listnode]:
        c=0
        curr=head
        while  curr:
            c+=1
            curr=curr.next
        mid=c//2
        curr=head
        for i in range(mid):
            curr=curr.next
        return curr    
        
#another method(hair and tortise method)#
class Solution:
    def middleNode(self,head:Optional[ListNode])->Optional[Listnode]:
        slow=fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        return slow    