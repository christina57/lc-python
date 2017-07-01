"""
361. Bomb Enemy

Given a 2D grid, each cell is either a wall 'W', an enemy 'E' or empty '0' (the number zero), return the maximum enemies you can kill using one bomb.
The bomb kills all the enemies in the same row and column from the planted point until it hits the wall since the wall is too strong to be destroyed.
Note that you can only put the bomb at an empty cell.

Example:
For the given grid

0 E 0 0
E 0 W E
0 E 0 0

return 3. (Placing a bomb at (1,1) kills 3 enemies)
"""

class Solution(object):
    def maxKilledEnemies(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        r = len(grid)
        if r == 0:
            return 0
        c = len(grid[0])
        
        rowdp = 0
        coldp = [0] * c
        res = 0
        
        for i in range(r):
            for j in range(c):
                if i == 0 or grid[i-1][j] == 'W':
                    coldp[j] = 0
                    idx = i
                    while idx < r and grid[idx][j] != 'W':
                        if grid[idx][j] == 'E':
                            coldp[j] += 1
                        idx += 1
                if j == 0 or grid[i][j-1] == 'W':
                    rowdp = 0
                    idx = j
                    while idx < c and grid[i][idx] != 'W':
                        if grid[i][idx] == 'E':
                            rowdp += 1
                        idx += 1
                if grid[i][j] == '0':
                    res = max(res, rowdp + coldp[j])
        
        return res
        