## 24. Swap Nodes in Pairs
## https://leetcode.com/problems/swap-nodes-in-pairs/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not(head) or not(head.next):
            return head
        tail = head
        head = tail.next
        tail.next = tail.next.next
        head.next = tail
        while tail.next and tail.next.next:
            temp1 = tail.next
            tail.next = tail.next.next
            temp1.next = tail.next.next
            tail.next.next = temp1
            tail = tail.next.next
        return head