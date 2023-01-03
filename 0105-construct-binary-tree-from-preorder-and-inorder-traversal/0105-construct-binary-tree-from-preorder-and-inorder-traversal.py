# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if inorder:
            index = inorder.index(preorder.pop(0)) #index is the current position in inorder
            root = TreeNode(inorder[index]) #make a new node
            root.left = self.buildTree(preorder, inorder[:index]) #left is everything before index
            root.right = self.buildTree(preorder, inorder[index+1:]) #right is everything after index
			
            return root

#inorder: insert nodes as they appear
#preorder: numerical order