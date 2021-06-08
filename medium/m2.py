class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry=0
        last=None
        first=None
        while((l1!=None)|(l2!=None)):
            firstNode=0
            secondNode=0
            if(l1):
                firstNode=l1.val
                l1=l1.next
            else:
                l1=None
            if(l2):
                secondNode=l2.val
                l2=l2.next
            else:
                l2=None
                
            sumVal=sum([carry,firstNode,secondNode])
            curr=ListNode(sumVal%10)
            carry=sumVal//10
            if(last):
                last.next=curr
            else:
                first=curr
            last=curr
            
        if(carry!=0):
            curr=ListNode(carry)
            last.next=curr
        return first
