class Solution:
    def ispalindrome(self,head: optional[ListNode]):
        if not head or not head.next:
            return True
        slow=fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        prev=None
        curr=slow
        while curr:
            nextN=curr.next
            curr.next=prev
            prev=curr
            curr=nextN    
        l,r=head,prev
        while r:
            if l.val!=r.val:
                return False
            l=l.next
            r=r.next
        return True    