"""

302. Smallest Rectangle Enclosing Black Pixels

An image is represented by a binary matrix with 0 as a white pixel and 1 as a black pixel. The black pixels are connected, i.e., there is only one black region. Pixels are connected horizontally and vertically. Given the location (x, y) of one of the black pixels, return the area of the smallest (axis-aligned) rectangle that encloses all black pixels.

For example, given the following image:

[
  "0010",
  "0110",
  "0100"
]
and x = 0, y = 2,
Return 6.

"""

class Solution(object):
    def minArea(self, image, x, y):
        """
        :type image: List[List[str]]
        :type x: int
        :type y: int
        :rtype: int
        """
        r = len(image)
        if r == 0:
            return 0
        c = len(image[0])
        
        up = self.binarysearch(image, 0, x, True, True)
        down = self.binarysearch(image, x+1, r, True, False)  
        left = self.binarysearch(image, 0, y, False, True)
        right = self.binarysearch(image, y+1, c, False, False)
        return (down - up) * (right - left)
    
    def binarysearch(self, image, start, end, isRow, asc):
        org = image if isRow else zip(*image)
        
        while start < end:
            mid = start + (end-start)/2
            if ('1' in org[mid]) ^ asc:
                start = mid + 1
            else:
                end = mid
        return start
     