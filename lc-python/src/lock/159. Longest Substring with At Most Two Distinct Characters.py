"""
159. Longest Substring with At Most Two Distinct Characters

Given a string, find the length of the longest substring T that contains at most 2 distinct characters.

For example, Given s = “eceba”,

T is "ece" which its length is 3.
"""
class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        dicts = {}
        res = 0
        cur = 0
        for i, c in enumerate(s):
            if c in dicts or len(dicts) < 2:
                cur += 1
            else:
                smallk = 0
                smallv = i
                for (k, v) in dicts.items():
                    if v < smallv:
                        smallk = k
                        smallv = v
                dicts.pop(smallk)
                cur = i - smallv
            res = max(res, cur)
            dicts[c] = i
        return res
                    