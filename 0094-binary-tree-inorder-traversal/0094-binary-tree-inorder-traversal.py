# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        def inorder(tree):
            if tree:
                #left, root, right
                inorder(tree.left)
                result.append(tree.val) #add nodes
                inorder(tree.right)
        
        inorder(root)
        return result