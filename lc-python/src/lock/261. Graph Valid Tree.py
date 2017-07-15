"""
261. Graph Valid Tree
Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), write a function to check whether these edges make up a valid tree.

For example:

Given n = 5 and edges = [[0, 1], [0, 2], [0, 3], [1, 4]], return true.

Given n = 5 and edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]], return false.

Note: you can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.

"""

class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        if n < 2:
            return True
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
        
        if len(dict) < n:
            return False
        
        visited = [False] * n
        visited[0] = True
        
        res = self.dfs(dict, visited, 0)
        if not res:
            return False
        if visited.count(True) < len(visited):
            return False
        return True
        
    def dfs(self, dict, visited, cur):
        
        for e in dict[cur]:
            if visited[e]:
                return False
            visited[e] = True
            dict[e].remove(cur)
            if not self.dfs(dict, visited, e):
                return False
        return True