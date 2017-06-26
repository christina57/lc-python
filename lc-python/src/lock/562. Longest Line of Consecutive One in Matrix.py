"""
562. Longest Line of Consecutive One in Matrix

Given a 01 matrix M, find the longest line of consecutive one in the matrix. The line could be horizontal, vertical, diagonal or anti-diagonal.

Example:
Input:
[[0,1,1,0],
 [0,1,1,0],
 [0,0,0,1]]
Output: 3
Hint: The number of elements in the given matrix will not exceed 10,000.
"""

class Solution(object):
    def longestLine(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        row = len(M)
        if row == 0:
            return 0
        col = len(M[0])
        
        # longest ending in current idx
        dp = [[[0] * 2 for _ in range(col)] for _ in range(row)]
        
        result = 0
        # left and up
        for r in range(row):
            for c in range(col):
                if M[r][c] == 1:
                    dp[r][c][0] = (dp[r][c-1][0] if c > 0 else 0) + 1
                    dp[r][c][1] = (dp[r-1][c][1] if r > 0 else 0) + 1
                    result = max(result, dp[r][c][0], dp[r][c][1])
                    
        # diagonal and anti-diagonal
        for r in range(row):
            for c in range(col-1, -1, -1):
                if M[r][c] == 1:
                    dp[r][c][0] = (dp[r-1][c-1][0] if r > 0 and c > 0 else 0) + 1
                    dp[r][c][1] = (dp[r-1][c+1][1] if r > 0  and c < (col-1) else 0) + 1
                    result = max(result, dp[r][c][0], dp[r][c][1])
                    
        return result