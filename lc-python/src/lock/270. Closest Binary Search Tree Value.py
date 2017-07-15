"""
270. Closest Binary Search Tree Value

Given a non-empty binary search tree and a target value, find the value in the BST that is closest to the target.

Note:
Given target value is a floating point.
You are guaranteed to have only one unique value in the BST that is closest to the target.

"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        
        if target < root.val and root.left is not None:
            left = self.closestValue(root.left, target)
            return left if abs(left - target) < abs(root.val - target) else root.val  
        elif target > root.val and root.right is not None:
            right = self.closestValue(root.right, target)
            return right if abs(right - target) < abs(root.val - target) else root.val
        else:
            return root.val