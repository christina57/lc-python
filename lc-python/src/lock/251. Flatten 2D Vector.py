"""
251. Flatten 2D Vector

Implement an iterator to flatten a 2d vector.

For example,
Given 2d vector =

[
  [1,2],
  [3],
  [4,5,6]
]
By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,2,3,4,5,6].

Follow up:
As an added challenge, try to code it using only iterators in C++ or iterators in Java.

"""

class Vector2D(object):

    def __init__(self, vec2d):
        """
        Initialize your data structure here.
        :type vec2d: List[List[int]]
        """
        self.vec2d = vec2d
        self.r = 0
        self.c = 0

    def next(self):
        """
        :rtype: int
        """
        if self.hasNext():
            self.c += 1
            return self.vec2d[self.r][self.c-1]

    def hasNext(self):
        """
        :rtype: bool
        """
        if len(self.vec2d) == 0:
            return False
        
        while self.r < len(self.vec2d) and self.c == len(self.vec2d[self.r]):
            self.r += 1
            self.c = 0
            
        if self.r >= len(self.vec2d):
            return False
         
        return True
        

# Your Vector2D object will be instantiated and called as such:
# i, v = Vector2D(vec2d), []
# while i.hasNext(): v.append(i.next())
# while i.hasNext(): v.append(i.next())