"""
356. Line Reflection
Given n points on a 2D plane, find if there is such a line parallel to y-axis that reflect the given points.

Example 1:
Given points = [[1,1],[-1,1]], return true.

Example 2:
Given points = [[1,1],[-1,-1]], return false.

Follow up:
Could you do better than O(n2)?
"""

class Solution(object):
    def isReflected(self, points):
        """
        :type points: List[List[int]]
        :rtype: bool
        """
        if len(points) == 0:
            return True
            
        s = sets.Set()
        xsum = 0
        cnt = 0
        for p in points:
            t = tuple(p)
            if t not in s:
                xsum += t[0]
                s.add(t)
                cnt += 1
        mid = float(xsum)/cnt
        
        while len(s) > 0:
            cur = s.pop()
            if cur[0] == mid:
                continue
            else:
                oppo = 2 * mid - cur[0]
                if (oppo, cur[1]) in s:
                    s.remove((oppo, cur[1]))
                else:
                    return False
        
        return True
        
        
        