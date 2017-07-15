"""
186. Reverse Words in a String II

Given an input string, reverse the string word by word. A word is defined as a sequence of non-space characters.

The input string does not contain leading or trailing spaces and the words are always separated by a single space.

For example,
Given s = "the sky is blue",
return "blue is sky the".

Could you do it in-place without allocating extra space?

Related problem: Rotate Array

"""

class Solution:
    # @param s, a list of 1 length strings, e.g., s = ['h','e','l','l','o']
    # @return nothing
    def reverseWords(self, s):
        s.reverse()
        
        idx = [i for i,c in enumerate(s) if c == ' ']
        idx.append(len(s))
        pre = 0
        for i in idx:
            s[pre:i] = reversed(s[pre:i])
            pre = i+1
        
            