"""
266. Palindrome Permutation

Given a string, determine if a permutation of the string could form a palindrome.

For example,
"code" -> False, "aab" -> True, "carerac" -> True.

"""

class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        counts = collections.Counter(s)
        
        odds = 0
        
        for v in counts.values():
            if v % 2 == 1:
                odds += 1
                if odds > 1:
                    return False
                
        return True