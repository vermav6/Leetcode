# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        lFinal = ListNode()
        currNode = lFinal
        while l1 and l2:
            if l1.val <= l2.val:
                currNode.next = l1
                l1 = l1.next
            else:
                currNode.next = l2
                l2 = l2.next
            currNode = currNode.next 
        if l1 is not None:
            currNode.next = l1
        else:
            currNode.next = l2
        return lFinal.next