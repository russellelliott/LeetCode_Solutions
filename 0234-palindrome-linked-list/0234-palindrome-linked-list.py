# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        
        numbers = []
        curr = head
        while(curr is not None):
            numbers.append(curr.val)
            curr = curr.next
        
        return numbers == numbers[::-1] # check if same front and back
        
#palindrome is the same forwards and backwards
#reverse linked list and compare to reverse