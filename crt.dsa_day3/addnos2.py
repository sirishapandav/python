class Solution:
    def addTwoNumbers(self,l1,l2):
        dummy=ListNode
        curr=dummy
        p1,p2=l1,l2
        c=0
        while p1 and p2:
            val=p1.val+p2.val+c
            c=val//10
            val=val%10
            curr.next=ListNode(val)
            curr=curr.next
            p1=p1.next
            p2=p2.next
        while p1:
            if c==1:
                val=p1.val+c
                c=val//10
                val=val%10
                curr.next=ListNode(val)
            else:
                curr.next=p1
                curr=curr.next
                p1=p1.next
        while p2:
            if c==1:
                val=p2.val+c
                c=val//10
                val=val%10
                curr.next=ListNode(val)
            else:
                curr.next=p1
                curr=curr.next
                p2=p2.next        
            if c==1:
                curr.next=ListNode(c)
            return dummy.next    
    
    
    


