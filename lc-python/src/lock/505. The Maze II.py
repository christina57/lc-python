"""
505. The Maze II

There is a ball in a maze with empty spaces and walls. The ball can go through empty spaces by rolling up, down, left or right, but it won't stop rolling until hitting a wall. When the ball stops, it could choose the next direction.

Given the ball's start position, the destination and the maze, find the shortest distance for the ball to stop at the destination. The distance is defined by the number of empty spaces traveled by the ball from the start position (excluded) to the destination (included). If the ball cannot stop at the destination, return -1.

The maze is represented by a binary 2D array. 1 means the wall and 0 means the empty space. You may assume that the borders of the maze are all walls. The start and destination coordinates are represented by row and column indexes.

Example 1

Input 1: a maze represented by a 2D array

0 0 1 0 0
0 0 0 0 0
0 0 0 1 0
1 1 0 1 1
0 0 0 0 0

Input 2: start coordinate (rowStart, colStart) = (0, 4)
Input 3: destination coordinate (rowDest, colDest) = (4, 4)

Output: 12
Explanation: One shortest way is : left -> down -> left -> down -> right -> down -> right.
             The total distance is 1 + 1 + 3 + 1 + 2 + 2 + 2 = 12.

Example 2

Input 1: a maze represented by a 2D array

0 0 1 0 0
0 0 0 0 0
0 0 0 1 0
1 1 0 1 1
0 0 0 0 0

Input 2: start coordinate (rowStart, colStart) = (0, 4)
Input 3: destination coordinate (rowDest, colDest) = (3, 2)

Output: -1
Explanation: There is no way for the ball to stop at the destination.

Note:
There is only one ball and one destination in the maze.
Both the ball and the destination exist on an empty space, and they will not be at the same position initially.
The given maze does not contain border (like the red rectangle in the example pictures), but you could assume the border of the maze are all walls.
The maze contains at least 2 empty spaces, and both the width and height of the maze won't exceed 100.
"""

import sys

class Solution(object):
    def shortestDistance(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: int
        """
        row = len(maze)
        if row == 0:
            return False
        col = len(maze[0])
        
        # -3 : not reachable, -2 : visited, -1 : default, >=0 distances
        dist = [[-1] * col for _ in range(row)]
        dist[start[0]][start[1]] = -2
        self.dfs(maze, start, destination, dist)
        return dist[start[0]][start[1]]
        
    def dfs(self, maze, start, destination, dist):
        print start, dist
        
        res = sys.maxsize
        exist = False
        for dire in range(4):
            ret = self.move(maze, start, dire)
            dest = ret[0]
            steps = ret[1]
            if dest == destination:
                dist[start[0]][start[1]] = steps
                return
            if dest == start or dist[dest[0]][dest[1]] == -2:
                continue
            if dist[dest[0]][dest[1]] == -1:
                dist[dest[0]][dest[1]] == -2
                self.dfs(maze, dest, destination, dist)
            if dist[dest[0]][dest[1]] >= 0:
                exist = True
                res = min(res, steps + dist[dest[0]][dest[1]])
                
        if exist:
            dist[start[0]][start[1]] = res
        else:
            dist[start[0]][start[1]] = -3
        
        
    # 0 up 1 down 2 left 3 right        
    def move(self, maze, start, direction):
        dires = [[-1,0],[1,0],[0,-1],[0,1]]
        
        #pass by reference
        cur = []
        cur.append(start[0])
        cur.append(start[1])
        steps = -1
        
        while (0 <= cur[0] < len(maze)) and (0<= cur[1] < len(maze[0])) and maze[cur[0]][cur[1]] != 1:
            cur[0] += dires[direction][0]
            cur[1] += dires[direction][1]
            steps += 1
            
        return [[cur[0] - dires[direction][0], cur[1] - dires[direction][1]], steps]


sol = Solution()
maze = [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]]
start = [0,4]
destination = [4,4]
print sol.shortestDistance(maze, start, destination)