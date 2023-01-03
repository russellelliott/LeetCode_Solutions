# Definition for singly-linked list.
#class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

    
class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        nodeList = set()
        node = head
        while(node):
            #if we've seen this node before, there is a cycle. return true
            if node in nodeList:
                return True
            
            #seeing node for first time? add it
            nodeList.add(node)
            
            #move on to next node
            node = node.next
        
        #No cycle? return false
        return False
        