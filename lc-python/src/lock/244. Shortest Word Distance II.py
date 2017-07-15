"""
244. Shortest Word Distance II

This is a follow up of Shortest Word Distance. The only difference is now you are given the list of words and your method will be called repeatedly many times with different parameters. How would you optimize it?

Design a class which receives a list of words in the constructor, and implements a method that takes two words word1 and word2 and return the shortest distance between these two words in the list.

For example,
Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

Given word1 = “coding”, word2 = “practice”, return 3.
Given word1 = "makes", word2 = "coding", return 1.

Note:
You may assume that word1 does not equal to word2, and word1 and word2 are both in the list.

"""
class WordDistance(object):

    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.dict = {}
        
        for i, v in enumerate(words):
            if v in self.dict:
                self.dict[v].append(i)
            else:
                self.dict[v] = [i]

    def shortest(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        idx1 = self.dict[word1]
        idx2 = self.dict[word2]
        
        i1 = i2 = 0
        res = abs(idx2[0] - idx1[0])
        
        while i1 < len(idx1) and i2 < len(idx2):
            res = min(res, abs(idx2[i2] - idx1[i1]))
            if idx1[i1] < idx2[i2]:
                i1 += 1
            else:
                i2 += 1
            
        return res
        
# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(words)
# param_1 = obj.shortest(word1,word2)