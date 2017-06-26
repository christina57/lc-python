"""
616. Add Bold Tag in String

Given a string s and a list of strings dict, you need to add a closed pair of bold tag <b> and </b> to wrap the substrings in s that exist in dict. If two such substrings overlap, you need to wrap them together by only one pair of closed bold tag. Also, if two substrings wrapped by bold tags are consecutive, you need to combine them.

Example 1:
Input: 
s = "abcxyz123"
dict = ["abc","123"]
Output:
"<b>abc</b>xyz<b>123</b>"
Example 2:
Input: 
s = "aaabbcc"
dict = ["aaa","aab","bc"]
Output:
"<b>aaabbc</b>c"
Note:
The given dict won't contain duplicates, and its length won't exceed 100.
All the strings in input have length in range [1, 1000].
"""

import re
class Solution(object):
    def addBoldTag(self, s, dict):
        """
        :type s: str
        :type dict: List[str]
        :rtype: str
        """
        if len(s) == 0 or len(dict) == 0:
            return s
            
        intervals = []
        for d in dict:
            pattern = r"(?=(" + d + r"))"
            matches = re.finditer(pattern, s)
            for match in matches:
                intervals.append([match.start(1), match.end(1)])
        
        intervals.sort(key=lambda x: x[0])
        
        if len(intervals) == 0:
            return s
            
        start, end = intervals[0]
        merged = []
        for i in range(1, len(intervals)):
            if intervals[i][0] <= end:
                end = max(intervals[i][1], end)
            else:
                merged.append(start)
                merged.append(end)
                start, end = intervals[i]
                
        merged.append(start)
        merged.append(end)
        
        slist = list(s)
        marker = True
        for i in reversed(merged):
            slist.insert(i, r"</b>" if marker else r"<b>")
            marker  =  not marker
            
        return "".join(slist)