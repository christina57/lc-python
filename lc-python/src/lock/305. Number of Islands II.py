"""

305. Number of Islands II

A 2d grid map of m rows and n columns is initially filled with water. We may perform an addLand operation which turns the water at position (row, col) into a land. Given a list of positions to operate, count the number of islands after each addLand operation. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example:

Given m = 3, n = 3, positions = [[0,0], [0,1], [1,2], [2,1]].
Initially, the 2d grid grid is filled with water. (Assume 0 represents water and 1 represents land).

0 0 0
0 0 0
0 0 0
Operation #1: addLand(0, 0) turns the water at grid[0][0] into a land.

1 0 0
0 0 0   Number of islands = 1
0 0 0
Operation #2: addLand(0, 1) turns the water at grid[0][1] into a land.

1 1 0
0 0 0   Number of islands = 1
0 0 0
Operation #3: addLand(1, 2) turns the water at grid[1][2] into a land.

1 1 0
0 0 1   Number of islands = 2
0 0 0
Operation #4: addLand(2, 1) turns the water at grid[2][1] into a land.

1 1 0
0 0 1   Number of islands = 3
0 1 0
We return the result as an array: [1, 1, 2, 3]

Challenge:

Can you do it in time complexity O(k log mn), where k is the length of the positions?

"""


class Solution(object):
    def numIslands2(self, m, n, positions):
        """
        :type m: int
        :type n: int
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        res = []
        if m < 1 or n < 1:
            return res
            
        lands = UnionFind()
        dirs = [(1,0),(-1,0),(0,1),(0,-1)]
        
        for pos in map(tuple, positions):
            lands.add(pos)
            for d in dirs:
                abj = (pos[0]+d[0], pos[1]+d[1])
                if abj in lands.id:
                    lands.unite(pos, abj)
            res.append(lands.count)
        
        return res
        
        
        
class UnionFind(object):
    def __init__(self):
        self.id = {}
        self.sz = {}
        self.count = 0
        
    def add(self, n):
        self.id[n] = n
        self.sz[n] = 1
        self.count += 1
        
    def getroot(self, n):
        par = self.id[n]
        cur = n
        while par != cur:
            self.id[cur] = self.id[par]
            par, cur = self.id[par], par
        return cur
    
    def unite(self, a, b):
        aroot = self.getroot(a)
        broot = self.getroot(b)
        
        if aroot != broot:
            if self.sz[aroot] > self.sz[broot]:
                aroot, broot = broot, aroot
            self.id[aroot] = broot
            self.sz[broot] += self.sz[aroot]
            self.count -= 1
            
        
        