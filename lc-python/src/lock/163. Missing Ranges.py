"""
163. Missing Ranges

Given a sorted integer array where the range of elements are in the inclusive range [lower, upper], return its missing ranges.

For example, given [0, 1, 3, 50, 75], lower = 0 and upper = 99, return ["2", "4->49", "51->74", "76->99"].

"""

class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        res = []
        
        start = lower
        end = lower
        
        for n in nums:
            if n > start:
                end = n - 1
                res.append(str(start) if start == end else str(start)+"->"+str(end))
            start = end = n+1
        
        if start != upper+1:
            end = upper
            res.append(str(start) if start == end else str(start)+"->"+str(end))
        return res