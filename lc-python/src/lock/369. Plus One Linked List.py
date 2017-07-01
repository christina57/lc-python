"""
369. Plus One Linked List
Given a non-negative integer represented as non-empty a singly linked list of digits, plus one to the integer.

You may assume the integer do not contain any leading zero, except the number 0 itself.

The digits are stored such that the most significant digit is at the head of the list.

Example:
Input:
1->2->3

Output:
1->2->4
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def plusOne(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        
        start9 = dummy
        end9 = dummy
        
        while end9.next is not None:
            end9 = end9.next
            if end9.val != 9:
                start9 = end9
        
        
        if end9.val != 9:
            end9.val += 1
        else:
            start9.val += 1
            start9 = start9.next
            while start9 is not None:
                start9.val = 0
                start9 = start9.next
        
        if dummy.val == 0:
            return head
        else:
            return dummy