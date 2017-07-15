"""

317. Shortest Distance from All Buildings

You want to build a house on an empty land which reaches all buildings in the shortest amount of distance. You can only move up, down, left and right. You are given a 2D grid of values 0, 1 or 2, where:

Each 0 marks an empty land which you can pass by freely.
Each 1 marks a building which you cannot pass through.
Each 2 marks an obstacle which you cannot pass through.
For example, given three buildings at (0,0), (0,4), (2,2), and an obstacle at (0,2):

1 - 0 - 2 - 0 - 1
|   |   |   |   |
0 - 0 - 0 - 0 - 0
|   |   |   |   |
0 - 0 - 1 - 0 - 0
The point (1,2) is an ideal empty land to build a house, as the total travel distance of 3+3+1=7 is minimal. So return 7.

Note:
There will be at least one building. If it is not possible to build such house according to the above rules, return -1.

"""

class Solution(object):
    def shortestDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        r = len(grid)
        if r == 0:
            return 0
        c = len(grid[0])
        
        total = [[0] * c for _ in range(r)]
        directions = [[-1,0],[1,0],[0,1],[0,-1]]
        
        for i in range(r):
            for j in range(c):
                if grid[i][j] == 1:
                    visited = [[False] * c for _ in range(r)]
                    sums = [[0] * c for _ in range(r)]
                    Q = collections.deque()
                    Q.append([i,j])
                    dis = 0
                    while Q:
                        size = len(Q)
                        dis += 1
                        for t in range(size):
                            cur = Q.popleft()
                            for d in directions:
                                a = cur[0] + d[0]
                                b = cur[1] + d[1]
                                if 0 <= a < r and 0 <= b < c and grid[a][b] == 0 and not visited[a][b] and total[a][b] != -1:
                                    sums[a][b] += dis
                                    visited[a][b] = True
                                    Q.append([a,b])
                    for p in range(r):
                        for q in range(c):
                            if grid[p][q] == 0:
                                if sums[p][q] == 0 or total[p][q] == -1:
                                    total[p][q] = -1
                                else:
                                    total[p][q] += sums[p][q]
                                
        
        res = sys.maxsize
        exist = False
        for i in range(r):
            for j in range(c):
                if grid[i][j] == 0 and total[i][j] != -1:
                    exist = True
                    res = min(res, total[i][j])
        return res if exist else -1