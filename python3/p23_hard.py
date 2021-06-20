## 23. Merge k Sorted Lists
## https://leetcode.com/problems/merge-k-sorted-lists/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from collections import deque
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        listDict = {}
        for li in lists:
            while li:
                if li.val in listDict.keys():
                    listDict[li.val] += 1
                else:
                    listDict[li.val] = 1
                li = li.next
        head = None
        tail = head
        for elem in sorted(listDict.keys()):
            for i in range(listDict[elem]):
                if head==None:
                    head = ListNode()
                    tail = head
                else:
                    tail.next = ListNode()
                    tail = tail.next
                tail.val = elem
        return head
    
    def mergeKLists2(self, lists: List[ListNode]) -> ListNode:
        if not(lists):
            return None
        lists = deque(lists)
        while len(lists)>1:
            l1 = lists.popleft()
            l2 = lists.popleft()
            lists.append(self.mergeTwoLists(l1,l2))
        return lists[0]
    
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
    