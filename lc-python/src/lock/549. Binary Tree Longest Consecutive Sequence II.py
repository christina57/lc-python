"""
549. Binary Tree Longest Consecutive Sequence II

Given a binary tree, you need to find the length of Longest Consecutive Path in Binary Tree.

Especially, this path can be either increasing or decreasing. For example, [1,2,3,4] and [4,3,2,1] are both considered valid, but the path [1,2,4,3] is not valid. On the other hand, the path can be in the child-Parent-child order, where not necessarily be parent-child order.

Example 1:
Input:
        1
       / \
      2   3
Output: 2
Explanation: The longest consecutive path is [1, 2] or [2, 1].
Example 2:
Input:
        2
       / \
      1   3
Output: 3
Explanation: The longest consecutive path is [1, 2, 3] or [3, 2, 1].
Note: All the values of tree nodes are in the range of [-1e7, 1e7].
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
        return self.helper(root)[2]
        
    def helper(self, root):
        # rtype: (int, int, int)
        # asc longest, desc longest to root, max consecutive
        if root is None:
            return (0, 0, 0)
        
        rootasc = rootdesc = rootcon = 1
        throughrootasc = throughrootdesc = 0
        
        if not root.left is None:
            (leftasc, leftdesc, leftcon) = self.helper(root.left)
            rootcon = max(rootcon, leftcon)
            if root.left.val == root.val - 1:
                rootasc = max(rootasc, leftasc + 1)
                throughrootasc += leftasc
            elif root.left.val == root.val + 1:
                rootdesc = max(rootdesc, leftdesc + 1)
                throughrootdesc += leftdesc
        
        if not root.right is None:
            (rightasc, rightdesc, rightcon) = self.helper(root.right)
            rootcon = max(rootcon, rightcon)
            if root.right.val == root.val - 1:
                rootasc = max(rootasc, rightasc + 1)
                throughrootdesc += rightasc
            elif root.right.val == root.val + 1:
                rootdesc = max(rootdesc, rightdesc + 1)
                throughrootasc += rightdesc
        
        rootcon = max(rootcon, throughrootasc+1, throughrootdesc+1)
        return (rootasc, rootdesc, rootcon)