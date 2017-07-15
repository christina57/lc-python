"""
246. Strobogrammatic Number

A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

Write a function to determine if a number is strobogrammatic. The number is represented as a string.

For example, the numbers "69", "88", and "818" are all strobogrammatic.

"""

class Solution(object):
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        left = 0
        right = len(num) - 1
        
        while left < right:
            if not((num[left] == num[right] and (num[left] == '1' or num[left] == '8' or num[left] == '0')) or (num[left] == '6' and num[right] == '9') or (num[left] == '9' and num[right] == '6')):
                return False
            left += 1
            right -= 1
        
        if left == right:
            return (num[left] == '1' or num[left] == '8' or num[left] == '0')
        return True
                