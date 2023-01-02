# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def length(self, head):
        count = 0
        temp = head
        while temp is not None:
            count+=1 #increment length
            temp = temp.next #go to next
        
        return count

    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        size = self.length(head)
        half = size//2
        
        temp = head
        for i in range(half):
            temp = temp.next
        
        return temp