## 19. Remove Nth Node From End of List
## https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        nthhead = head
        tail = head
        count = 0
        while tail:
            tail = tail.next
            if not(tail):
                if nthhead==head and count==n-1:
                    head = head.next
                else:
                    nthhead.next = nthhead.next.next
            count+=1
            
            if count>n:
                nthhead = nthhead.next
        return head