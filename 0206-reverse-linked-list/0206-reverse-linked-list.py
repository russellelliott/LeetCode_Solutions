# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if(head==None):
            return
        
        curr = head #current node
        after = None #node after current node
        before = None #node before current node
        
        #reverse nodes
        while(curr is not None):
            after = curr.next
            curr.next = before
            before = curr
            curr = after
        
        head = before
        
        return head