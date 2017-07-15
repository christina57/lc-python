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

        Q = collections.deque()
        Q.append(start)

        dire = ((0, 1), (0, -1), (1, 0), (-1, 0))
        dist = [[sys.maxsize] * col for _ in range(row)]
        dist[start[0]][start[1]] = 0

        while Q:
            size = len(Q)
            for i in range(size):
                cur = Q.popleft()
                for d in dire:
                    (end, steps) = self.move(maze, cur, d)
                    if (dist[cur[0]][cur[1]] + steps) < dist[end[0]][end[1]]:
                        dist[end[0]][end[1]] = dist[cur[0]][cur[1]] + steps
                        Q.append(end)

        if dist[destination[0]][destination[1]] < sys.maxsize:
            return dist[destination[0]][destination[1]]
        else:
            return -1

    def move(self, maze, start, dires):
        # pass by reference
        cur = []
        cur.append(start[0])
        cur.append(start[1])
        steps = -1

        while (0 <= cur[0] < len(maze)) and (0 <= cur[1] < len(maze[0])) and maze[cur[0]][cur[1]] != 1:
            cur[0] += dires[0]
            cur[1] += dires[1]
            steps += 1

        return ((cur[0] - dires[0], cur[1] - dires[1]), steps)