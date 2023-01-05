# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        before = head
        current = head
        headTemp = head
        
        #edge case 1: n is the length of the linked list
        node = head
        length = 0
        while node:
            node = node.next
            length = length+1
        #if we reached the end, return node after
        if length==n:
            return head.next
        
        head = headTemp
        
        #go n times to set the before
        for i in range(length-n-1):
            before = before.next
            #current = current.next
        #current = current.next #move again
        
        #set the node after before to the node after current
        #before.next = current.next
        before.next = before.next.next
        
        #reset head
        head = headTemp
        return head