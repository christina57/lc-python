"""

411. Minimum Unique Word Abbreviation

A string such as "word" contains the following abbreviations:

["word", "1ord", "w1rd", "wo1d", "wor1", "2rd", "w2d", "wo2", "1o1d", "1or1", "w1r1", "1o2", "2r1", "3d", "w3", "4"]
Given a target string and a set of strings in a dictionary, find an abbreviation of this target string with the smallest possible length such that it does not conflict with abbreviations of the strings in the dictionary.

Each number or letter in the abbreviation is considered length = 1. For example, the abbreviation "a32bc" has length = 4.

Note:
In the case of multiple answers as shown in the second example below, you may return any one of them.
Assume length of target string = m, and dictionary size = n. You may assume that m ≤ 21, n ≤ 1000, and log2(n) + m ≤ 20.
Examples:
"apple", ["blade"] -> "a4" (because "5" or "4e" conflicts with "blade")

"apple", ["plain", "amber", "blade"] -> "1p3" (other valid answers include "ap3", "a3e", "2p2", "3le", "3l1").

"""

class Solution(object):
    def minAbbreviation(self, target, dictionary):
        """
        :type target: str
        :type dictionary: List[str]
        :rtype: str
        """
        lens = len(target)
        dict = []
        for w in dictionary:
            num = 0
            if len(w) == lens:
                for i, c in enumerate(w):
                    if c != target[i]:
                        num += (1 << (len(w) - 1 - i))
                dict.append(num)

        if not dict:
            return str(lens)

        cand = []
        total = reduce(lambda a, b: a | b, dict)
        i = 0
        while total > 0:
            if total & 1 == 1:
                cand.append(i)
            i += 1
            total /= 2

        self.minlen = len(target) + 1
        self.minval = 0
        self.dfs(dict, cand, 0, 0, target)
        return self.getOrgStr(target, self.minval)

    def getOrgStr(self, target, bits):
        res = []
        zeros = 0
        i = 0
        cur = bits
        while i < len(target):
            if cur & 1 == 1:
                if zeros > 0:
                    res.append(str(zeros))
                res.append(target[len(target) - 1 - i])
                zeros = 0
            else:
                zeros += 1
            cur /= 2
            i += 1
        if zeros > 0:
            res.append(str(zeros))
        return "".join(res[::-1])

    def getAbbrlen(self, target, abbrbit):
        res = 0
        zeros = 0
        i = 0
        cur = abbrbit
        while i < len(target):
            if cur & 1 == 1:
                res += (1 + zeros)
                zeros = 0
            else:
                zeros = 1
            cur /= 2
            i += 1

        res += zeros
        return res

    def dfs(self, dict, cand, idx, cur, target):
        if idx == len(cand):
            for d in dict:
                if d & cur == 0:
                    return
            le = self.getAbbrlen(target, cur)
            if le < self.minlen:
                self.minlen = le
                self.minval = cur
        else:
            newcur = cur + (1 << cand[idx])
            if self.getAbbrlen(target, newcur) < self.minlen:
                self.dfs(dict, cand, idx + 1, newcur, target)
                self.dfs(dict, cand, idx + 1, cur, target)
            elif self.getAbbrlen(target, cur) < self.minlen:
                self.dfs(dict, cand, idx + 1, cur, target)    