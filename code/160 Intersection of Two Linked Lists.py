# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        nodesA = []
        nodesB = []
        while headA:
            nodesA.append(headA)
            headA = headA.next
        while headB:
            nodesB.append(headB)
            headB = headB.next
        res = None
        while nodesA and nodesB:
            nodeA = nodesA.pop()
            nodeB = nodesB.pop()
            if nodeA is nodeB:
                res = nodeA
            else:
                break
        return res


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        p = headA
        q = headB
        while p is not q:
            if p:
                p = p.next
            else:
                p = headB
            if q:
                q = q.next
            else:
                q = headA
        return p
