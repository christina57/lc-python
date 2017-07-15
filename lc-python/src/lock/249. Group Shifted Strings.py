"""

249. Group Shifted Strings

Given a string, we can "shift" each of its letter to its successive letter, for example: "abc" -> "bcd". We can keep "shifting" which forms the sequence:

"abc" -> "bcd" -> ... -> "xyz"
Given a list of strings which contains only lowercase alphabets, group all strings that belong to the same shifting sequence.

For example, given: ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"], 
A solution is:

[
  ["abc","bcd","xyz"],
  ["az","ba"],
  ["acef"],
  ["a","z"]
]

"""

class Solution(object):
    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        dict = {}
        
        for s in strings:
            offset = []
            for c in s:
                offset.append(chr(ord(c)-ord(s[0])+ord('a')+(26 if c < s[0] else 0)))
            st = "".join(offset)
            if dict.has_key(st):
                dict[st].append(s)
            else:
                dict[st] = [s]
        return dict.values()