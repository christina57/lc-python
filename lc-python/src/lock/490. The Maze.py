"""
490. The Maze

There is a ball in a maze with empty spaces and walls. The ball can go through empty spaces by rolling up, down, left or right, but it won't stop rolling until hitting a wall. When the ball stops, it could choose the next direction.

Given the ball's start position, the destination and the maze, determine whether the ball could stop at the destination.

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

Output: true
Explanation: One possible way is : left -> down -> left -> down -> right -> down -> right.

Example 2

Input 1: a maze represented by a 2D array

0 0 1 0 0
0 0 0 0 0
0 0 0 1 0
1 1 0 1 1
0 0 0 0 0

Input 2: start coordinate (rowStart, colStart) = (0, 4)
Input 3: destination coordinate (rowDest, colDest) = (3, 2)

Output: false
Explanation: There is no way for the ball to stop at the destination.

Note:
There is only one ball and one destination in the maze.
Both the ball and the destination exist on an empty space, and they will not be at the same position initially.
The given maze does not contain border (like the red rectangle in the example pictures), but you could assume the border of the maze are all walls.
The maze contains at least 2 empty spaces, and both the width and height of the maze won't exceed 100.
"""
class Solution(object):
    def hasPath(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: bool
        """
        row = len(maze)
        if row == 0:
            return False
        col = len(maze[0])
        
        used = [[False] * col for _ in range(row)]
        used[start[0]][start[1]] = True
        return self.dfs(maze, start, destination, used)
        
        
        
        """
        cand = []
        cand.append(start)
        
        while len(cand) > 0:
            cur = cand.pop()
            if used[cur[0]][cur[1]]:
                continue
            used[cur[0]][cur[1]] = True
            for dire in range(4):
                dest = self.move(maze, cur, dire)
                if dest != [-1,-1] and not used[dest[0]][dest[1]]:
                    cand.append(dest)
                    if dest == destination and self.iswall(maze, dest, dire):
                        return True
        return False
        """
    
    def dfs(self, maze, start, destination, used):
        for dire in range(4):
            dest = self.move(maze, start, dire)
            if dest == destination:
                return True
            if dest != [-1,-1] and not used[dest[0]][dest[1]]:
                used[dest[0]][dest[1]] = True
                if self.dfs(maze, dest, destination, used):
                    return True
        return False
        
    # 0 up 1 down 2 left 3 right        
    def move(self, maze, start, direction):
        dires = [[-1,0],[1,0],[0,-1],[0,1]]
        
        cur = start
        movable = False
        while 0 <= cur[0] < len(maze) and 0<= cur[1] < len(maze[0]) and maze[cur[0]][cur[1]] != 1:
            cur[0] += dires[direction][0]
            cur[1] += dires[direction][1]
            movable = True
        
        if movable:
            return [cur[0] - dires[direction][0], cur[1] - dires[direction][1]]
        else:
            return [-1,-1]
        