"""
291. Word Pattern II

Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty substring in str.

Examples:
pattern = "abab", str = "redblueredblue" should return true.
pattern = "aaaa", str = "asdasdasdasd" should return true.
pattern = "aabb", str = "xyzabcxzyabc" should return false.
Notes:
You may assume both pattern and str contains only lowercase letters.


"""

class Solution(object):
    def wordPatternMatch(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        maps = {}
        vset = set()
        return self.helper(pattern, 0, str, 0, maps, vset)
    
    def helper(self, pattern, pidx, str, sidx, maps, vset):
        if pidx == len(pattern) and sidx == len(str):
            return True
        elif pidx == len(pattern) or sidx == len(str):
            return False
            
        p = pattern[pidx]
        if p in maps:
            v = maps[p]
            if v == str[sidx:sidx+len(v)]:
                return self.helper(pattern, pidx+1, str, sidx+len(v), maps, vset)
            else:
                return False
        else:
            for i in range(1, len(str)-sidx+2-len(pattern)+pidx):
                if str[sidx:sidx+i] in vset:
                    continue
                maps[p] = str[sidx:sidx+i]
                vset.add(str[sidx:sidx+i])
                if self.helper(pattern, pidx+1, str, sidx+i, maps, vset):
                    return True
                del maps[p]
                vset.discard(str[sidx:sidx+i])
            return False
            
        