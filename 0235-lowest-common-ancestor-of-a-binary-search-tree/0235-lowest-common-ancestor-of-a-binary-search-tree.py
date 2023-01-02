# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        
        #nodes will exist. no need to check if one exists or not
        #if both less, recurse left
        if p.val < root.val and q.val < root.val and root.left is not None:
            return self.lowestCommonAncestor(root.left, p, q)
        elif p.val > root.val and q.val > root.val and root.right is not None:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root
#a least common ancestor of p and q is a node in between them