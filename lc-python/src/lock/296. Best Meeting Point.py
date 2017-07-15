"""

296. Best Meeting Point

A group of two or more people wants to meet and minimize the total travel distance. You are given a 2D grid of values 0 or 1, where each 1 marks the home of someone in the group. The distance is calculated using Manhattan Distance, where distance(p1, p2) = |p2.x - p1.x| + |p2.y - p1.y|.

For example, given three people living at (0,0), (0,4), and (2,2):

1 - 0 - 0 - 0 - 1
|   |   |   |   |
0 - 0 - 0 - 0 - 0
|   |   |   |   |
0 - 0 - 1 - 0 - 0
The point (0,2) is an ideal meeting point, as the total travel distance of 2+2+2=6 is minimal. So return 6.

"""

class Solution(object):
    def minTotalDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows = []
        cols = []
        
        r = len(grid)
        if r == 0:
            return 0
        c = len(grid[0])
        
        for i in range(r):
            for j in range(c):
                if grid[i][j] == 1:
                    rows.append(i)
                    
        for j in range(c):
            for i in range(r):
                if grid[i][j] == 1:
                    cols.append(j)

        res = 0
        rl = len(rows)
        for i in range(rl/2):
            res += rows[rl-i-1] - rows[i]
            
        cl = len(cols)
        for i in range(cl/2):
            res += cols[cl-i-1] - cols[i]
            
        return res