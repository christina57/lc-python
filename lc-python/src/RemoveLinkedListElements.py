# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        cur = head
        pre = head
        while(cur != None):
            if(cur.val == val):
                if(cur == head):
                    head = cur.next
                    pre = head
                else :
                    pre.next = cur.next
            else:
                pre = cur
            cur = cur.next
        return head       
        