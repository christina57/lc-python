"""
469. Convex Polygon

Given a list of points that form a polygon when joined sequentially, find if this polygon is convex (Convex polygon definition).

Note:

There are at least 3 and at most 10,000 points.
Coordinates are in the range -10,000 to 10,000.
You may assume the polygon formed by given points is always a simple polygon (Simple polygon definition). In other words, we ensure that exactly two edges intersect at each vertex, and that edges otherwise don't intersect each other.
Example 1:

[[0,0],[0,1],[1,1],[1,0]]

Answer: True

Explanation:
Example 2:

[[0,0],[0,10],[10,10],[10,0],[5,5]]

Answer: False

Explanation:
"""

class Solution(object):
    def isConvex(self, points):
        """
        :type points: List[List[int]]
        :rtype: bool
        """
        prev = 0
        for i in range(0, len(points)):
            p0 = points[i]
            p1 = points[(i+1)%len(points)]
            p2 = points[(i+2)%len(points)]
            
            direction = (p1[0] - p0[0]) * (p2[1] - p0[1]) - (p2[0] -p0[0]) * (p1[1] - p0[1])
            
            if direction == 0:
                continue
            if prev * direction < 0:
                return False
                
            prev = direction
        return True