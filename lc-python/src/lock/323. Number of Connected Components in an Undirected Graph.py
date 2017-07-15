"""
323. Number of Connected Components in an Undirected Graph

Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), write a function to find the number of connected components in an undirected graph.

Example 1:
     0          3
     |          |
     1 --- 2    4
Given n = 5 and edges = [[0, 1], [1, 2], [3, 4]], return 2.

Example 2:
     0           4
     |           |
     1 --- 2 --- 3
Given n = 5 and edges = [[0, 1], [1, 2], [2, 3], [3, 4]], return 1.

Note:
You can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.

"""

class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        dict = {}
        
        for e in edges:
            if dict.has_key(e[0]):
                dict[e[0]].append(e[1])
            else:
                dict[e[0]] = [e[1]]
            if dict.has_key(e[1]):
                dict[e[1]].append(e[0])
            else:
                dict[e[1]] = [e[0]]
                
        visited = [False] * n
        res = 0
        
        for num in range(n):
            if not visited[num]:
                self.dfs(num, dict, visited)
                res += 1
        return res
    
    def dfs(self, cur, dict, visited):
        visited[cur] = True
        
        if not dict.has_key(cur):
            return
        abj = dict[cur]
        
        for i in abj:
            if not visited[i]:
                self.dfs(i, dict, visited)
        