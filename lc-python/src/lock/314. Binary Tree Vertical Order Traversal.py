"""
314. Binary Tree Vertical Order Traversal

Given a binary tree, return the vertical order traversal of its nodes' values. (ie, from top to bottom, column by column).

If two nodes are in the same row and column, the order should be from left to right.

Examples:

Given binary tree [3,9,20,null,null,15,7],
   3
  /\
 /  \
 9  20
    /\
   /  \
  15   7
return its vertical order traversal as:
[
  [9],
  [3,15],
  [20],
  [7]
]
Given binary tree [3,9,8,4,0,1,7],
     3
    /\
   /  \
   9   8
  /\  /\
 /  \/  \
 4  01   7
return its vertical order traversal as:
[
  [4],
  [9],
  [3,0,1],
  [8],
  [7]
]
Given binary tree [3,9,8,4,0,1,7,null,null,null,2,5] (0's right child is 2 and 1's left child is 5),
     3
    /\
   /  \
   9   8
  /\  /\
 /  \/  \
 4  01   7
    /\
   /  \
   5   2
return its vertical order traversal as:
[
  [4],
  [9,5],
  [3,0,1],
  [8,2],
  [7]
]

"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        
        Q = []
        Q.append((root,0))
        res = [[root.val]]
        
        while len(Q) > 0:
            size = len(Q)
            offset = 0
            for i in range(size):
                item = Q.pop(0)
                cur = item[0]
                idx = item[1]
                if cur.left is not None:
                    if idx == 0:
                        res.insert(0, [cur.left.val])
                        offset = 1
                    else:
                        res[idx+offset-1].append(cur.left.val)
                    Q.append((cur.left, idx+offset-1))
                if cur.right is not None:
                    if idx+offset == len(res)-1:
                        res.append([cur.right.val])
                    else:
                        res[idx+offset+1].append(cur.right.val)
                    Q.append((cur.right, idx+offset+1))
          
        return res