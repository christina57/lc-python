"""

340. Longest Substring with At Most K Distinct Characters


Given a string, find the length of the longest substring T that contains at most k distinct characters.

For example, Given s = “eceba” and k = 2,

T is "ece" which its length is 3.

"""

class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        """
        :type s: str
        :rtype: int
        """
        if k == 0:  
            return 0
        dicts = collections.defaultdict(int)
        res = 0
        start = 0
        nums = 0
        
        for i, c in enumerate(s):
            if c not in dicts:
                while nums >= k:
                    dicts[s[start]] -= 1
                    if dicts[s[start]] == 0:
                        dicts.pop(s[start])
                        nums -= 1
                    start += 1
                nums += 1
            res = max(res, i - start + 1)
            dicts[c] += 1
        return res