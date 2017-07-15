"""
243. Shortest Word Distance

Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.

For example,
Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

Given word1 = “coding”, word2 = “practice”, return 3.
Given word1 = "makes", word2 = "coding", return 1.

Note:
You may assume that word1 does not equal to word2, and word1 and word2 are both in the list.

"""
class Solution(object):
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        i1 = -1
        i2 = -1
        res = len(words)
        for i, w in enumerate(words):
            if w == word1:
                i1 = i
                if i2 != -1:
                    res = min(res, abs(i - i2))
            elif w == word2:
                i2 = i
                if i1 != -1:
                    res = min(res, abs(i - i1))
        return res