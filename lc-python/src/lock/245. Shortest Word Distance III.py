"""
245. Shortest Word Distance III

This is a follow up of Shortest Word Distance. The only difference is now word1 could be the same as word2.

Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.

word1 and word2 may be the same and they represent two individual words in the list.

For example,
Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

Given word1 = “makes”, word2 = “coding”, return 1.
Given word1 = "makes", word2 = "makes", return 3.

Note:
You may assume word1 and word2 are both in the list.

"""

class Solution(object):
    def shortestWordDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        res = len(words)
        i1 = -res
        i2 = -res
        isSame = (word1 == word2)
        
        for i, w in enumerate(words):
            if isSame and w == word1:
                i1, i2 = i2, i
                res = min(res, abs(i2 - i1))
            else:
                if w == word1:
                    i1 = i
                    if i2 != -1:
                        res = min(res, abs(i - i2))
                elif w == word2:
                    i2 = i
                    if i1 != -1:
                        res = min(res, abs(i - i1))
        return res
    