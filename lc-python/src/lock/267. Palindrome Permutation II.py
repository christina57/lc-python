"""
267. Palindrome Permutation II

Given a string s, return all the palindromic permutations (without duplicates) of it. Return an empty list if no palindromic permutation could be form.

For example:

Given s = "aabb", return ["abba", "baab"].

Given s = "abc", return [].

"""

class Solution(object):
    def generatePalindromes(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        counts = collections.Counter(s)
        
        odds = 0
        oddv = ""
        slist = []
        for k, v in counts.items():
            if v % 2 == 1:
                oddv = k
                odds += 1
                if odds > 1:
                    return []
            for i in range(v/2):
                slist.append(k)
       
        res = []
        used = [False] * len(slist)
        item = []
        self.helper(slist, item, res, used, oddv)
        return res
        
    def helper(self, slist, item, res, used, oddv):
        if len(item) == len(slist):
            res.append("".join(item) + oddv + "".join(item[::-1]))
        else:
            for i in range(len(slist)):
                if (i == 0 or slist[i-1] != slist[i] or used[i-1]) and not used[i]:
                    used[i] = True
                    item.append(slist[i])
                    self.helper(slist, item, res, used, oddv)
                    used[i] = False
                    item.pop(-1)
                    