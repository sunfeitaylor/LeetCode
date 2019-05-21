# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        res = ListNode(0)
        p = res
        while l1 or l2:
            if l1 and l2:
                val1 = l1.val
                val2 = l2.val
                if val1 < val2:
                    p.next = ListNode(val1)
                    l1 = l1.next
                else:
                    p.next = ListNode(val2)
                    l2 = l2.next
            elif l1:
                p.next = l1
                break
            else:
                p.next = l2
                break
            p = p.next
        return res.next


# recursion solution
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        if not l2:
            return l1
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2
