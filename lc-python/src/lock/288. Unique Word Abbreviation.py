"""
288. Unique Word Abbreviation

An abbreviation of a word follows the form <first letter><number><last letter>. Below are some examples of word abbreviations:

a) it                      --> it    (no abbreviation)

     1
b) d|o|g                   --> d1g

              1    1  1
     1---5----0----5--8
c) i|nternationalizatio|n  --> i18n

              1
     1---5----0
d) l|ocalizatio|n          --> l10n
Assume you have a dictionary and given a word, find whether its abbreviation is unique in the dictionary. A word's abbreviation is unique if no other word from the dictionary has the same abbreviation.

Example: 
Given dictionary = [ "deer", "door", "cake", "card" ]

isUnique("dear") -> 
false

isUnique("cart") -> 
true

isUnique("cane") -> 
false

isUnique("make") -> 
true


"""

class ValidWordAbbr(object):

    def __init__(self, dictionary):
        """
        :type dictionary: List[str]
        """
        self.se = {}
        self.dict = sets.Set(dictionary)
        for st in self.dict:
            l = len(st)
            abbr = (st[0] + str(l-2) + st[-1]) if l > 2 else st
            self.se[abbr] = self.se.get(abbr, 0) + 1
                

    def isUnique(self, word):
        """
        :type word: str
        :rtype: bool
        """
        l = len(word)
        abbr = (word[0] + str(l-2) + word[-1]) if l > 2 else word
        
        if abbr not in self.se:
            return True
        
        sameabbr = self.se[abbr]
        
        if word in self.dict:
            sameabbr -= 1
        
        if sameabbr > 0:
            return False
        else:
            return True
        


# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param_1 = obj.isUnique(word)