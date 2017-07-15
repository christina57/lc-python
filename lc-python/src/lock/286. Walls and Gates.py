"""
286. Walls and Gates

You are given a m x n 2D grid initialized with these three possible values.

-1 - A wall or an obstacle.
0 - A gate.
INF - Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.
Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.

For example, given the 2D grid:
INF  -1  0  INF
INF INF INF  -1
INF  -1 INF  -1
  0  -1 INF INF
After running your function, the 2D grid should be:
  3  -1   0   1
  2   2   1  -1
  1  -1   2  -1
  0  -1   3   4
  
"""
  
  
class Solution(object):
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: void Do not return anything, modify rooms in-place instead.
        """
        
        r = len(rooms)
        if r == 0:
            return 
        c = len(rooms[0])
        
        for i in range(r):
            for j in range(c):
                if rooms[i][j] == 0:
                    self.bfs(rooms, i, j)
                    
        
    def bfs(self, rooms, i, j):
        Q = []
        Q.append((i,j))
        layer = 0
        direct = ((-1,0),(1,0),(0,1),(0,-1))
        
        while len(Q) >0:
            size = len(Q)
            
            for i in range(size):
                cur = Q.pop(0)
                if rooms[cur[0]][cur[1]] > layer:
                    rooms[cur[0]][cur[1]] = layer
                    
                for j in range(4):
                    if 0 <= cur[0]+direct[j][0] < len(rooms) and 0 <= cur[1]+direct[j][1] < len(rooms[0]) and rooms[cur[0]+direct[j][0]][cur[1]+direct[j][1]] > layer:
                        Q.append((cur[0]+direct[j][0], cur[1]+direct[j][1]))
            layer += 1
            