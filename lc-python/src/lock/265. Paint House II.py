"""
265. Paint House II

There are a row of n houses, each house can be painted with one of the k colors. The cost of painting each house with a certain color is different. You have to paint all the houses such that no two adjacent houses have the same color.

The cost of painting each house with a certain color is represented by a n x k cost matrix. For example, costs[0][0] is the cost of painting house 0 with color 0; costs[1][2] is the cost of painting house 1 with color 2, and so on... Find the minimum cost to paint all houses.

Note:
All costs are positive integers.

Follow up:
Could you solve it in O(nk) runtime?
"""

class Solution(object):
    def minCostII(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        hozcnt = len(costs)
        if hozcnt == 0:
            return 0
        colcnt = len(costs[0])
        # first smallest, second smallest, first idx, second idx
        mins = [0, 0, -1, -1]
        
        for i in range(0, hozcnt):
            cmins = [sys.maxsize, sys.maxsize, -1, -1]
            for j in range(colcnt):
                if j != mins[2]:
                    cur = mins[0] + costs[i][j]
                else:
                    cur = mins[1] + costs[i][j]
                if cur < cmins[0]:
                    cmins[0], cmins[1], cmins[2], cmins[3] = cur, cmins[0], j, cmins[2] 
                elif cur < cmins[1]:
                    cmins[1], cmins[3] = cur, j
            mins = cmins    
                 
                    
        return mins[0]
        