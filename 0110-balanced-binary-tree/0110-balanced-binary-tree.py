# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        #height of a node
        def height(node):
            if node is None:
                return 0
            else:
                return 1 + max(height(node.left), height(node.right))
        
        
        if root is None:
            return True
        
        #if difference in subtree heights is at most 1 and the left and right subtrees are balanced
        return self.isBalanced(root.left) and self.isBalanced(root.right) and abs(height(root.left)-height(root.right))<=1
            

#a tree is balanced if the left and right subtree are dirrerent in height by at most 1