"""
247. Strobogrammatic Number II

A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

Find all strobogrammatic numbers that are of length = n.

For example,
Given n = 2, return ["11","69","88","96"].
"""

class Solution(object):
    def findStrobogrammatic(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        item = [0] * n
        res = []
        maps = [[0,0],[1,1],[8,8],[6,9],[9,6]]
        self.helper(n, 0, item, res, maps)
        return res
        
    def helper(self, n, idx, item, res, maps):
        if idx == n/2:
            if n%2 == 1:
                for i in [1,8,0]:
                    item[n/2] = i
                    res.append("".join(map(str,item)))
            else:
                res.append("".join(map(str,item)))
        else:
            for pair in maps:
                if idx == 0 and pair[0] == 0:
                    continue
                item[idx] = pair[0]
                item[n-1-idx] = pair[1]
                self.helper(n, idx+1, item, res, maps)