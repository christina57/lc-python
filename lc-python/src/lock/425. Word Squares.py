"""

425. Word Squares


Given a set of words (without duplicates), find all word squares you can build from them.

A sequence of words forms a valid word square if the kth row and column read the exact same string, where 0 ≤ k < max(numRows, numColumns).

For example, the word sequence ["ball","area","lead","lady"] forms a word square because each word reads the same both horizontally and vertically.

b a l l
a r e a
l e a d
l a d y
Note:
There are at least 1 and at most 1000 words.
All words will have the exact same length.
Word length is at least 1 and at most 5.
Each word contains only lowercase English alphabet a-z.
Example 1:

Input:
["area","lead","wall","lady","ball"]

Output:
[
  [ "wall",
    "area",
    "lead",
    "lady"
  ],
  [ "ball",
    "area",
    "lead",
    "lady"
  ]
]

Explanation:
The output consists of two word squares. The order of output does not matter (just the order of words in each word square matters).
Example 2:

Input:
["abat","baba","atan","atal"]

Output:
[
  [ "baba",
    "abat",
    "baba",
    "atan"
  ],
  [ "baba",
    "abat",
    "baba",
    "atal"
  ]
]

Explanation:
The output consists of two word squares. The order of output does not matter (just the order of words in each word square matters).
"""

class Solution(object):
    def wordSquares(self, words):
        """
        :type words: List[str]
        :rtype: List[List[str]]
        """
        wlen = len(words[0])
        item = [None] * wlen
        res = []

        trie = Trie()
        for i, w in enumerate(words):
            trie.addWord(w, i)

        self.helper(words, item, res, 0, wlen, trie)
        return res

    def helper(self, words, item, res, idx, wlen, trie):
        if idx == wlen:
            res.append(list(item))
        elif idx == 0:
            for w in words:
                item[idx] = w
                self.helper(words, item, res, idx + 1, wlen, trie)
        else:
            prefix = zip(*(item[:idx]))[idx]
            pre = trie.findPrefix(prefix)
            if pre is not None:
                for i in pre.idx:
                    item[idx] = words[i]
                    self.helper(words, item, res, idx + 1, wlen, trie)


class Trie(object):
    def __init__(self):
        self.root = Node()

    def addWord(self, word, i):
        cur = self.root
        for ch in word:
            cur.idx.append(i)
            ich = ord(ch) - ord('a')
            if not cur.children[ich]:
                cur.children[ich] = Node()
            cur = cur.children[ich]

    def findPrefix(self, prefix):
        cur = self.root
        for ch in prefix:
            ich = ord(ch) - ord('a')
            if cur.children[ich]:
                cur = cur.children[ich]
            else:
                return None
        return cur


class Node(object):
    def __init__(self):
        self.idx = []
        self.children = [None] * 26