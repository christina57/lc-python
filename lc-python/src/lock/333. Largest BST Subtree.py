"""
333. Largest BST Subtree
Given a binary tree, find the largest subtree which is a Binary Search Tree (BST), where largest means subtree with largest number of nodes in it.

Note:
A subtree must include all of its descendants.
Here's an example:
    10
    / \
   5  15
  / \   \ 
 1   8   7
The Largest BST Subtree in this case is the highlighted one. 
The return value is the subtree's size, which is 3.
Follow up:
Can you figure out ways to solve it with O(n) time complexity?
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def largestBSTSubtree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        
        return self.helper(root)[3]
        
    def helper(self, root):
    # return (smallest, biggest, isBST, largestBST)
        if root.left is None and root.right is None:
            return (root.val, root.val, True, 1)
        
        isBST = True
        leftBST = 0
        rightBST = 0
        smallest = biggest = root.val
        if root.left is not None:
            l = self.helper(root.left)
            smallest = min(smallest, l[0])
            if not l[2] or l[1] >= root.val:
                isBST = False
            leftBST = l[3]
            
        if root.right is not None:
            r = self.helper(root.right)
            biggest = max(biggest, r[1])
            if not isBST or not r[2] or r[0] <= root.val:
                isBST = False
            rightBST = r[3]
            
        largestBST = (1+leftBST+rightBST) if isBST else max(leftBST, rightBST)
        
        return (smallest, biggest, isBST, largestBST)