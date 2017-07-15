"""
320. Generalized Abbreviation

Write a function to generate the generalized abbreviations of a word.

Example:
Given word = "word", return the following list (order does not matter):
["word", "1ord", "w1rd", "wo1d", "wor1", "2rd", "w2d", "wo2", "1o1d", "1or1", "w1r1", "1o2", "2r1", "3d", "w3", "4"]
"""

class Solution(object):
    def generateAbbreviations(self, word):
        """
        :type word: str
        :rtype: List[str]
        """
        res = []
        item = []
        self.helper(word, 0, item, res)
        return res
        
    def helper(self, word, idx, item, res):
        if idx == len(word):
            res.append("".join(item))
            return
        
        item.append(word[idx])
        self.helper(word, idx+1, item, res)
        item.pop(-1)
        
        if len(item) == 0 or not item[-1].isdigit():
            for i in range(1, len(word) - idx + 1):
                item.append(str(i))
                self.helper(word, idx+i, item, res)
                item.pop(-1)
    
        