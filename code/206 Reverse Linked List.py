# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        cur = head
        while cur is not None:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        return prev


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not (head and head.next):
            return head
        p = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return p


class Solution:
    def reverseList(self, head: ListNode, prev=None) -> ListNode:
        if not head:
            return prev
        temp = head.next
        head.next = prev
        prev = head
        head = temp
        return self.reverseList(head, prev)
