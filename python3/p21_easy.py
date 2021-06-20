## 21. Merge Two Sorted Lists
## https://leetcode.com/problems/merge-two-sorted-lists/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1:
            if l2:
                if l1.val >l2.val:
                    l1,l2 = l2,l1
            else:
                return l1
        else:
            return l2
            
        mergel = l1
        while l1.next and l2:
            if l2.val < l1.next.val:
                temp = l1.next
                l1.next = l2
                l2 = temp
            # print(l1.val)
            l1 = l1.next
        if l2:
            l1.next = l2
        return mergel