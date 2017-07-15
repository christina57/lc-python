"""

527. Word Abbreviation
Given an array of n distinct non-empty strings, you need to generate minimal possible abbreviations for every word following rules below.

Begin with the first character and then the number of characters abbreviated, which followed by the last character.
If there are any conflict, that is more than one words share the same abbreviation, a longer prefix is used instead of only the first character until making the map from word to abbreviation become unique. In other words, a final abbreviation cannot map to more than one original words.
If the abbreviation doesn't make the word shorter, then keep it as original.
Example:
Input: ["like", "god", "internal", "me", "internet", "interval", "intension", "face", "intrusion"]
Output: ["l2e","god","internal","me","i6t","interval","inte4n","f2e","intr4n"]
Note:
Both n and the length of each word will not exceed 400.
The length of each word is greater than 1.
The words consist of lowercase English letters only.
The return answers should be in the same order as the original array.

"""

class Solution(object):
    def wordsAbbreviation(self, dict):
        """
        :type dict: List[str]
        :rtype: List[str]
        """
        res = [None] * len(dict)
        
        #create a trie for each first+last+len
        lendict = collections.defaultdict(list)
        for i, word in enumerate(dict):
            l = len(word)
            if l > 3:
                lendict[word[0]+word[-1]+str(l)].append((word, i))
            else:
                res[i] = word
                
        def longest_common_prefix(a, b):
            i = 0
            while i < len(a) and i < len(b) and a[i] == b[i]:
                i += 1
            return i
    
        for group in lendict.values():
            if len(group) == 1:
                word = group[0][0]
                res[group[0][1]] = word[:1] + str(len(word)-2) + word[-1]
            else:
                group.sort()
                lcp = [0] * len(group)
                for i, (w1, w2) in enumerate(zip(group, group[1:])):
                    idx = longest_common_prefix(w1[0], w2[0])
                    lcp[i] = max(idx, lcp[i])
                    lcp[i+1] = max(idx, lcp[i+1])
                
                for i in range(len(group)):
                    word = group[i][0]
                    idx = group[i][1]
                    prefix = lcp[i]
                    if len(word) - prefix > 3:
                        res[idx] = word[:prefix+1] + str(len(word)-prefix-2) + word[-1]
                    else:
                        res[idx] = word
        return res