## 25. Reverse Nodes in k-Group
## https://leetcode.com/problems/reverse-nodes-in-k-group/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if k<2:
            return head
        kGroup = []
        temp = head
        while temp and len(kGroup)<k:
            kGroup.append(temp)
            temp = temp.next
        if len(kGroup)<k:
            return head
        head = kGroup.pop()
        tail = head
        while kGroup:
            tail.next = kGroup.pop()
            tail = tail.next
        tail.next = temp
        while True:
            temp = tail.next
            while temp and len(kGroup)<k:
                kGroup.append(temp)
                temp = temp.next
            if len(kGroup)<k:
                # return head
                break 
            while kGroup:
                tail.next = kGroup.pop()
                tail = tail.next
            tail.next = temp
        return head

