"""

250. Count Univalue Subtrees

Given a binary tree, count the number of uni-value subtrees.

A Uni-value subtree means all nodes of the subtree have the same value.

For example:
Given binary tree,
              5
             / \
            1   5
           / \   \
          5   5   5
return 4.

"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countUnivalSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.helper(root)[1]
        
    # return [isUni, count]
    def helper(self, root):
        if root is None:
            return [True, 0]
            
        left = self.helper(root.left)
        right = self.helper(root.right)
        
        cnt = left[1] + right[1]
        isUni = False
        if left[0] and right[0] and (root.left is None or root.left.val == root.val) and (root.right is None or root.right.val == root.val):
            isUni = True
            cnt += 1
        return [isUni, cnt]
        
        