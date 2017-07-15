"""
269. Alien Dictionary

There is a new alien language which uses the latin alphabet. However, the order among letters are unknown to you. You receive a list of non-empty words from the dictionary, where words are sorted lexicographically by the rules of this new language. Derive the order of letters in this language.

Example 1:
Given the following words in dictionary,

[
  "wrt",
  "wrf",
  "er",
  "ett",
  "rftt"
]
The correct order is: "wertf".

Example 2:
Given the following words in dictionary,

[
  "z",
  "x"
]
The correct order is: "zx".

Example 3:
Given the following words in dictionary,

[
  "z",
  "x",
  "z"
]
The order is invalid, so return "".

Note:
You may assume all letters are in lowercase.
You may assume that if a is a prefix of b, then a must appear before b in the given dictionary.
If the order is invalid, return an empty string.
There may be multiple valid order of letters, return any one of them is fine.
"""

class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        indegree = collections.defaultdict(set)
        outdegree = collections.defaultdict(set)
        for pair in zip(words, words[1:]):
            for c1, c2 in zip(*pair):
                if c1 != c2:
                    indegree[c2].add(c1)
                    outdegree[c1].add(c2)
                    break
        total = set("".join(words))
        zeroin = total - set(indegree)
        res = []
        while zeroin:
            n = zeroin.pop()
            res.append(n)
            for abj in outdegree[n]:
                indegree[abj].discard(n)
                if len(indegree[abj]) == 0:
                    zeroin.add(abj)
            
        if len(res) == len(total):
            return "".join(res)
        else:
            return ""
            