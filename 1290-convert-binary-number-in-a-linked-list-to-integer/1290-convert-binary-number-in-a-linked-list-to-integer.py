# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def getDecimalValue(self, binary):
        """
        :type head: ListNode
        :rtype: int
        """
        number = ""
        node = binary
        while(node):
            number = "".join([number, str(node.val)])
            node = node.next
        print(number)

        #convert to binary
        binary = int(number, 2)
        print(binary)
        return binary