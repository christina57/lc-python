"""
346. Moving Average from Data Stream

Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.

For example,
MovingAverage m = new MovingAverage(3);
m.next(1) = 1
m.next(10) = (1 + 10) / 2
m.next(3) = (1 + 10 + 3) / 3
m.next(5) = (10 + 3 + 5) / 3
"""

class MovingAverage(object):

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.window = [0,0,0]
        self.cnt = 0
        self.idx = 0
        self.total = 0

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        self.total += (val - self.window[self.idx])
        self.window[self.idx] = val
        self.idx += 1
        if self.cnt < 3:
            self.cnt += 1
        
        return self.total/self.cnt


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)