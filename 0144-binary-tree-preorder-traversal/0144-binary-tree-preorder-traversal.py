# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        def preorder(tree):
            if tree:
                #root, left, right
                result.append(tree.val) #add nodes
                preorder(tree.left)
                preorder(tree.right)
        
        preorder(root)
        return result