# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
import heapq


# Heap solution.
class Solution:
    def mergeKLists(self, lists):
        sentinel = ListNode(0)
        current = sentinel
        head = []
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(head, (lists[i].val, i))
                lists[i] = lists[i].next
        while head:
            val, idx = heapq.heappop(head)
            current.next = ListNode(val)
            current = current.next
            if lists[idx]:
                heapq.heappush(head, (lists[idx].val, idx))
                lists[idx] = lists[idx].next
        return sentinel.next


# Divide and conquer solution.
class Solution:
    def mergeKLists(self, lists):
        if not lists:
            return None
        sentinel = ListNode(0)
        while len(lists) > 1:
            merged = []
            while len(lists) > 1:
                merged.append(self.merge(lists.pop(), lists.pop(), sentinel))
            lists += merged
        return lists[0]

    def merge(self, x, y, sentinel):
        current = sentinel
        while x and y:
            if x.val < y.val:
                current.next = x
                x = x.next
            else:
                current.next = y
                y = y.next
            current = current.next
        current.next = x if x else y
        return sentinel.next
