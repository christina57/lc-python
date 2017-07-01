"""
408. Valid Word Abbreviation

Given a non-empty string s and an abbreviation abbr, return whether the string matches with the given abbreviation.

A string such as "word" contains only the following valid abbreviations:

["word", "1ord", "w1rd", "wo1d", "wor1", "2rd", "w2d", "wo2", "1o1d", "1or1", "w1r1", "1o2", "2r1", "3d", "w3", "4"]
Notice that only the above abbreviations are valid abbreviations of the string "word". Any other string is not a valid abbreviation of "word".

Note:
Assume s contains only lowercase letters and abbr contains only lowercase letters and digits.

Example 1:
Given s = "internationalization", abbr = "i12iz4n":

Return true.
Example 2:
Given s = "apple", abbr = "a2e":

Return false.
"""

class Solution(object):
    def validWordAbbreviation(self, word, abbr):
        """
        :type word: str
        :type abbr: str
        :rtype: bool
        """
        idx1 = 0
        idx2 = 0
        
        while idx1 < len(word) and idx2 < len(abbr):
            if 'a' <= abbr[idx2] <= 'z':
                if word[idx1] == abbr[idx2]:
                    idx1 += 1
                    idx2 += 1
                else:
                    return False
            else:
                if abbr[idx2] == '0':
                    return False
                start = idx2
                while idx2+1 < len(abbr) and '0' <= abbr[idx2+1] <= '9':
                    idx2 +=1
                idx2 += 1
                cnt = int(abbr[start:idx2])
                idx1 += cnt
                
        return idx1 ==len(word) and idx2 == len(abbr)