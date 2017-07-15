"""

308. Range Sum Query 2D - Mutable

Given a 2D matrix matrix, find the sum of the elements inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).

Range Sum Query 2D
The above rectangle (with the red border) is defined by (row1, col1) = (2, 1) and (row2, col2) = (4, 3), which contains sum = 8.

Example:
Given matrix = [
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
]

sumRegion(2, 1, 4, 3) -> 8
update(3, 2, 2)
sumRegion(2, 1, 4, 3) -> 10
Note:
The matrix is only modifiable by the update function.
You may assume the number of calls to update and sumRegion function is distributed evenly.
You may assume that row1 ≤ row2 and col1 ≤ col2.

"""

class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        self.r = len(matrix)
        if self.r == 0:
            return
        self.c = len(matrix[0])
        self.nums = [[0] * self.c for _ in range(self.r)]
        self.bit = [[0] * (self.c+1) for _ in range(self.r+1)]
        for i in range(self.r):
            for j in range(self.c):
                self.update(i, j, matrix[i][j])

    def update(self, row, col, val):
        """
        :type row: int
        :type col: int
        :type val: int
        :rtype: void
        """
        if self.r == 0:
            return
        diff = val - self.nums[row][col]
        self.nums[row][col] = val
        i = row + 1
        while i <= self.r:
            j = col + 1
            while j <= self.c:
                self.bit[i][j] += diff
                j += j & (-j)
            i += i & (-i)

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        if self.r == 0:
            return 0
        return self.sumhelper(row2+1, col2+1) + self.sumhelper(row1, col1) - self.sumhelper(row1, col2+1) - self.sumhelper(row2+1, col1)
        
    def sumhelper(self, row, col):
        res = 0
        i = row
        while i > 0:
            j = col
            while j > 0:
                res += self.bit[i][j]
                j -= j & (-j)
            i -= i & (-i)
        return res
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# obj.update(row,col,val)
# param_2 = obj.sumRegion(row1,col1,row2,col2)