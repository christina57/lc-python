import sys

import collections


class Solution(object):
    def findShortestWay(self, maze, ball, hole):
        """
        :type maze: List[List[int]]
        :type ball: List[int]
        :type hole: List[int]
        :rtype: str
        """
        row = len(maze)
        if row == 0:
            return False
        col = len(maze[0])

        Q = collections.deque()
        Q.append(ball)

        dire = ((1, 0), (0, -1), (0, 1), (-1, 0))
        diresym = ('d', 'l', 'r', 'u')
        distpath = [[[sys.maxsize, []] for _ in range(col)] for _ in range(row)]
        distpath[ball[0]][ball[1]][0] = 0
        mindist = sys.maxsize
        path = []

        while Q:
            cur = Q.popleft()
            for i, d in enumerate(dire):
                steps = 0
                next = [cur[0], cur[1]]
                while (0 <= next[0] < len(maze)) and (0 <= next[1] < len(maze[0])) and maze[next[0]][next[1]] != 1:
                    if next == hole:
                        if (distpath[cur[0]][cur[1]][0] + steps) < mindist or ((distpath[cur[0]][cur[1]][0] + steps) == mindist and distpath[cur[0]][cur[1]][1]+[diresym[i]] < path):
                            mindist = (distpath[cur[0]][cur[1]][0] + steps)
                            path = distpath[cur[0]][cur[1]][1]+[diresym[i]]

                    next[0] += d[0]
                    next[1] += d[1]
                    steps += 1
                steps -= 1
                end = (next[0] - d[0], next[1] - d[1])

                if (distpath[cur[0]][cur[1]][0] + steps) < distpath[end[0]][end[1]][0] or ((distpath[cur[0]][cur[1]][0] + steps) == distpath[end[0]][end[1]][0] and distpath[cur[0]][cur[1]][1]+[diresym[i]] < distpath[end[0]][end[1]][1]):
                    distpath[end[0]][end[1]][0] = distpath[cur[0]][cur[1]][0] + steps
                    distpath[end[0]][end[1]][1] = distpath[cur[0]][cur[1]][1]+[diresym[i]]
                    Q.append(end)

        if mindist < sys.maxsize:
            return "".join(path)
        else:
            return "impossible"



sol = Solution()
maze = [[0,1,0,0,1,0,0,0,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0],[0,0,0,0,0,1,0,0,1,0,0,1,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,1],[0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,0,0,0,1,0,0],[1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,0,0,0,0,0,0,1,0,0,1,0,0,1,0,0],[0,1,0,0,1,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0],[0,0,1,0,0,1,0,0,1,0,0,1,0,0,0,0,0,1,0,0,1,0,0,1,0,0,0,0,0,0],[0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,1,0,0,1,0,0],[1,0,0,1,0,0,1,0,0,1,0,0,0,0,0,1,0,0,1,0,0,0,0,0,1,0,0,1,0,0],[0,1,0,0,0,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,0,0,0,1,0,0,1,0],[0,0,1,0,0,1,0,0,1,0,0,1,0,0,0,0,0,1,0,0,0,0,0,1,0,0,1,0,0,1],[0,0,0,1,0,0,1,0,0,1,0,0,0,0,0,1,0,0,1,0,0,0,0,0,1,0,0,1,0,0],[1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,0,0,0,1,0,0,1,0,0],[0,1,0,0,1,0,0,0,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0],[0,0,1,0,0,1,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,1,0,0,1,0,0,1],[0,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,0,0,0],[1,0,0,0,0,0,0,0,0,1,0,0,1,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,1,0,0,1,0,0,1,0,0,1,0,0,0,0,0,1,0,0,1,0,0,1,0,0,1,0],[0,0,1,0,0,1,0,0,1,0,0,1,0,0,0,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1],[0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,1,0,0],[1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0],[0,1,0,0,1,0,0,1,0,0,0,0,0,1,0,0,1,0,0,1,0,0,0,0,0,0,0,0,1,0],[0,0,1,0,0,1,0,0,1,0,0,0,0,0,1,0,0,0,0,0,1,0,0,1,0,0,0,0,0,1],[0,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,0,0,0],[1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0],[0,1,0,0,1,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,1,0,0,1,0,0,0,0],[0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1],[0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,1,0,0,1,0,0],[1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0],[0,1,0,0,1,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,1,0,0,1,0,0,1,0],[0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,0,0,0,1,0,0,1,0,0,1]]
start = [29,18]
destination = [14,22]
print sol.findShortestWay(maze, start, destination)