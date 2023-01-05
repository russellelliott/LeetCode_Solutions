# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        node = head
        length = 0
        while node:
            node = node.next
            length = length+1
        
        print("length: ", length)
        #edge case for lists of length 1; will return empty list, as the middle node is the only node
        if length==1:
            return head.next
        
        node = head
        #go floor(length/2) times forward in list)
        for i in range(length//2-1):
            node = node.next
        
        #perform the delete
        node.next = node.next.next
        
        return head

#delete middle node
#first, find length
#then go to length/2 node

#if length is 2, middle is 2 (use floor?)

#reused: https://leetcode.com/problems/remove-nth-node-from-end-of-list/submissions/