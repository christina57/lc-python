"""
158. Read N Characters Given Read4 II - Call multiple times
The API: int read4(char *buf) reads 4 characters at a time from a file.

The return value is the actual number of characters read. For example, it returns 3 if there is only 3 characters left in the file.

By using the read4 API, implement the function int read(char *buf, int n) that reads n characters from the file.

Note:
The read function may be called multiple times.
"""

# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):

class Solution(object):
    
    def __init__(self):
        self.extra = []
    
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        tmp = [None] * 4
        while True:
            red = read4(tmp)
            if red == 0:
                cnt = min(n, len(self.extra))
                buf[:cnt] = self.extra[:cnt]
                self.extra = self.extra[cnt:]
                return cnt
            else:
                self.extra.extend(tmp[:red])
                if n <= len(self.extra):
                    buf[:n] = self.extra[:n]
                    self.extra = self.extra[n:]
                    return n