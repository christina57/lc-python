"""
358. Rearrange String k Distance Apart

Given a non-empty string s and an integer k, rearrange the string such that the same characters are at least distance k from each other.

All input strings are given in lowercase letters. If it is not possible to rearrange the string, return an empty string "".

Example 1:
s = "aabbcc", k = 3

Result: "abcabc"

The same letters are at least distance 3 from each other.
Example 2:
s = "aaabc", k = 3 

Answer: ""

It is not possible to rearrange the string.
Example 3:
s = "aaadbbcc", k = 2

Answer: "abacabcd"

Another possible answer is: "abcabcda"

The same letters are at least distance 2 from each other.

"""

class Solution(object):
    def rearrangeString(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        lens = len(s)
        if lens < 2 or k < 2:
            return s
        
        # map idx to chars, chars will be available at idx
        avail = collections.defaultdict(set)
        
        # map char to cnt
        cnts = collections.defaultdict(int)
        for c in s:
            cnts[c] -= 1
            avail[0].add(c)
        
        maxheap = []
        idx = 0
        res = [None] * lens
        
        while idx < lens:
            if avail[idx]:
                for c in avail[idx]:
                    heapq.heappush(maxheap, (cnts[c],c))
            if maxheap:
                cur = heapq.heappop(maxheap)[1]
                res[idx] = cur
                cnts[cur] += 1
                if cnts[cur] < 0:
                    avail[idx + k].add(cur)
            else:
                return ""
            idx += 1
            
            
        return "".join(res)
        
        
        