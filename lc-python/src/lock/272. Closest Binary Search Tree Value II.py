"""
272. Closest Binary Search Tree Value II

Given a non-empty binary search tree and a target value, find k values in the BST that are closest to the target.

Note:
Given target value is a floating point.
You may assume k is always valid, that is: k ≤ total nodes.
You are guaranteed to have only one unique set of k values in the BST that are closest to the target.
Follow up:
Assume that the BST is balanced, could you solve it in less than O(n) runtime (where n = total nodes)?

"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def closestKValues(self, root, target, k):
        """
        :type root: TreeNode
        :type target: float
        :type k: int
        :rtype: List[int]
        """
        if root is None:
            return []
        left = self.closestKValues(root.left, target, k)
        right = self.closestKValues(root.right, target, k)
        
        res = left + [root.val] + right
        if len(res) <= k:
            return res
        else:
            dif = len(res) - k
            left = 0
            right = len(res) - 1
            while dif > 0:
                if abs(res[left] - target) < abs(res[right] - target):
                    right -= 1
                else:
                    left += 1
                dif -= 1
            return res[left:right+1]
        
        