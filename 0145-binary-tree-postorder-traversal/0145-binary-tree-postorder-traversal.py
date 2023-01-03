# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        def postorder(tree):
            if tree:
                #left, right, root
                postorder(tree.left)
                postorder(tree.right)
                result.append(tree.val) #add nodes
        
        postorder(root)
        return result