"""
366. Find Leaves of Binary Tree

Given a binary tree, collect a tree's nodes as if you were doing this: Collect and remove all leaves, repeat until the tree is empty.

Example:
Given binary tree 
          1
         / \
        2   3
       / \     
      4   5    
Returns [4, 5, 3], [2], [1].

Explanation:
1. Removing the leaves [4, 5, 3] would result in this tree:

          1
         / 
        2          
2. Now removing the leaf [2] would result in this tree:

          1          
3. Now removing the leaf [1] would result in the empty tree:

          []         
Returns [4, 5, 3], [2], [1].
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        dict = {}
        height = self.path(root,dict)
        print height
        print dict
        res = list(list())
        for i in range(1,height+1):
            res.append(dict[i])
        return res
        
    def path(self, root, dict):
        if root is None:
            return 0
   
        res = max(self.path(root.left,dict),self.path(root.right,dict)) + 1
        if dict.has_key(res):
            dict[res].append(root.val)
        else:
            dict[res] = [root.val]
        return res
            