"""
298. Binary Tree Longest Consecutive Sequence

Given a binary tree, find the length of the longest consecutive sequence path.

The path refers to any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The longest consecutive path need to be from parent to child (cannot be the reverse).

For example,
   1
    \
     3
    / \
   2   4
        \
         5
Longest consecutive sequence path is 3-4-5, so return 3.
   2
    \
     3
    / 
   2    
  / 
 1
Longest consecutive sequence path is 2-3,not3-2-1, so return 2.

"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.helper(root, 1)
        
    def helper(self, root, tocur):
        if root is None:
            return 0
        
        maxpath = 0
        ltocur = rtocur = tocur
        if root.left is not None and root.val + 1 == root.left.val:
            ltocur += 1
        else:
            ltocur = 1
        if root.right is not None and root.val + 1 == root.right.val:
            rtocur += 1
        else:
            rtocur = 1
        l = self.helper(root.left, ltocur)
        r = self.helper(root.right, rtocur)
        
        return max(l, r, tocur)
        
            
            
        