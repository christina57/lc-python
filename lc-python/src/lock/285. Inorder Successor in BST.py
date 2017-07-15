"""
285. Inorder Successor in BST

Given a binary search tree and a node in it, find the in-order successor of that node in the BST.

Note: If the given node has no in-order successor in the tree, return null.

"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        return self.successor(root, p)
    
    def successor(self, root, p):
        if root is None:
            return None
            
        if root.val <= p.val:
            return self.successor(root.right, p)
        else:
            res = self.successor(root.left, p)
            return res if res is not None else root
            
    
    def predecessor(self, root, p):
        if root is None:
            return None
            
        if root.val >= p.val:
            return self.predecessor(root.left, p)
        else:
            res = self.predecessor(root.right, p)
            return res if res is not None else root