"""
161. One Edit Distance

Given two strings S and T, determine if they are both one edit distance apart.
"""
class Solution(object):
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        slen = len(s)
        tlen = len(t)
        
        if slen == tlen:
            for i in range(slen):
                if s[i] != t[i]:
                    return s[i+1:] == t[i+1:]
            return False
        elif abs(slen - tlen) == 1:
            lon = s
            short = t
            if slen < tlen:
                lon = t
                short = s
            for i in range(len(short)):
                if short[i] != lon[i]:
                    return short[i:] == lon[i+1:]
            return True
        else:
            return False
        
        