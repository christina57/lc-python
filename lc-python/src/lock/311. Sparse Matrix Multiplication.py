"""
311. Sparse Matrix Multiplication
Given two sparse matrices A and B, return the result of AB.

You may assume that A's column number is equal to B's row number.

Example:

A = [
  [ 1, 0, 0],
  [-1, 0, 3]
]

B = [
  [ 7, 0, 0 ],
  [ 0, 0, 0 ],
  [ 0, 0, 1 ]
]


     |  1 0 0 |   | 7 0 0 |   |  7 0 0 |
AB = | -1 0 3 | x | 0 0 0 | = | -7 0 3 |
                  | 0 0 1 |
                  
"""

class Solution(object):
    def multiply(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        ra = len(A)
        if ra == 0:
            return []
        ca = len(A[0])
        if ca == 0:
            return []
        rb = len(B)
        if rb == 0:
            return []
        cb = len(B[0])
        if cb == 0:
            return []
        
        res = [[0] * cb for _ in range(ra)]
        
        for a1 in range(ra):
            for a2 in range(ca):
                if A[a1][a2] != 0:
                    for b2 in range(cb):
                        if B[a2][b2] != 0:
                            res[a1][b2] += A[a1][a2] * B[a2][b2]
                            
        return res
        