"""
255. Verify Preorder Sequence in Binary Search Tree

Given an array of numbers, verify whether it is the correct preorder traversal sequence of a binary search tree.

You may assume each number in the sequence is unique.

Follow up:
Could you do it using only constant space complexity?

"""
class Solution(object):
    def verifyPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: bool
        """
        small = -sys.maxsize-1
        stack = []
        
        for i in preorder:
            if i < small:
                return False
            while len(stack) > 0 and i > stack[-1]:
                small = stack.pop(-1)
            stack.append(i)
            
        return True