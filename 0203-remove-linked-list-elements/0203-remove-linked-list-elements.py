# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        
        def removeFirstInstance(head, val):
            if head==None:
                return
            
            prev = None
            curr = head
            #while we can move forward and not at index
            while curr and curr.val!=val:
                prev = curr #previous node
                curr = curr.next #current node
            
            print(curr.val)
            if prev==None:
                head = head.next
                print("delete at head")
            else:
                prev.next = curr.next
                
            return head
            
            
        '''def deleteAtPosition(head, position):
            if head == None:
                return
            
            index = 0
            curr = head
            #while we can move forward and not at index
            while curr.next and index<position:
                prev = curr #previous node
                curr = curr.next #current node
                index+=1 #move index
            
            if index==0:
                head = head.next #delete at head, set head to the node after
            else:
                prev.next = curr.next #node before it skips over current node
            
            return head'''
                
        #remove nodes that have a given value
        node = head
        
        #first. collect all indexes of that number
        #indexes = []
        numIndexes = 0
        index = 0
        while node:
            if node.val == val:
                #indexes.append(index)
                numIndexes+=1
            #move on
            index+=1
            node = node.next
        
        #print("indexes: ", indexes)
        
        '''for i in indexes:
            head = deleteAtPosition(head, i)'''
        
        for i in range(numIndexes):
            head = removeFirstInstance(head, val)
        
        return head
#reused: https://leetcode.com/problems/remove-nth-node-from-end-of-list/submissions/
#reused: https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/submissions/

'''
if the current node has value
    if head, set head to head.next
    if other node, set next of node before to next of node
'''

#delete linked list node at current index
#find indexes of all the nodes of that value

#issue: position of number changes in linked list. this will cause the wrong nodes to be deleted in some cases
#solution: delete the first instance of the node for the amount of times it appears