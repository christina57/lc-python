"""
531. Lonely Pixel I

Given a picture consisting of black and white pixels, find the number of black lonely pixels.

The picture is represented by a 2D char array consisting of 'B' and 'W', which means black and white pixels respectively.

A black lonely pixel is character 'B' that located at a specific position where the same row and same column don't have any other black pixels.

Example:
Input: 
[['W', 'W', 'B'],
 ['W', 'B', 'W'],
 ['B', 'W', 'W']]

Output: 3
Explanation: All the three 'B's are black lonely pixels.
Note:
The range of width and height of the input 2D array is [1,500].
"""

class Solution(object):
    def findLonelyPixel(self, picture):
        """
        :type picture: List[List[str]]
        :rtype: int
        """
        row = len(picture)
        if row == 0:
            return 0
        col = len(picture[0])
        
        dict = {}
        result = 0
        
        for i in range(row):
            if picture[i].count('B') == 1:
                idx = picture[i].index('B')
                cnt = 0
                for j in range(row):
                    cnt += (1 if picture[j][idx] == 'B' else 0)
                    
                if cnt == 1:
                    result += 1
        
        return result           