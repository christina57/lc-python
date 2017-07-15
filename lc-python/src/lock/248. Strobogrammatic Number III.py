"""
 
248. Strobogrammatic Number III

A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

Write a function to count the total strobogrammatic numbers that exist in the range of low <= num <= high.

For example,
Given low = "50", high = "100", return 3. Because 69, 88, and 96 are three strobogrammatic numbers.

Note:
Because the range might be a large number, the low and high numbers are represented as string.
"""

class Solution(object):
    def strobogrammaticInRange(self, low, high):
        """
        :type low: str
        :type high: str
        :rtype: int
        """
        llen = len(low)
        hlen = len(high)
        maps = [[0,0],[1,1],[6,9],[8,8],[9,6]]
        
        start = ""
        end = ""
        res = 0
        for n in range(llen,hlen+1):
            if n != llen and n != hlen:
                if n%2 == 0:
                    res += 4 * pow(5, n/2-1)
                else:
                    if n == 1:
                        res += 3
                    else:
                        res += 12 * pow(5, (n-3)/2)
                continue
            if n == llen:
                start = low
            else:
                start = "1" + "0" * (n-1)
            if n == hlen:
                end = high
            else:
                end = "9" * n
            
            item = [0] * n
            res += self.helper(0, n-1, item, start, end, maps)

        return res                
                
    def helper(self, left, right, item, start, end, maps):     
        if left <= right:
            cnt = 0
            for j in range(5):
                if left == 0 and right != 0 and j == 0:
                    continue
                if left == right and (j == 2 or j == 4):
                    continue
                item[left] = maps[j][0]
                item[right] = maps[j][1]
                cnt += self.helper(left+1, right-1, item, start, end, maps)
            return cnt
        else:
            if start <= "".join(map(str,item)) <= end:
                return 1
            else:
                return 0