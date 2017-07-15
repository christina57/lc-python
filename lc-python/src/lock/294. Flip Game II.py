"""
294. Flip Game II

You are playing the following Flip Game with your friend: Given a string that contains only these two characters: + and -, you and your friend take turns to flip two consecutive "++" into "--". The game ends when a person can no longer make a move and therefore the other person will be the winner.

Write a function to determine if the starting player can guarantee a win.

For example, given s = "++++", return true. The starting player can guarantee a win by flipping the middle "++" to become "+--+".

Follow up:
Derive your algorithm's runtime complexity.
"""

class Solution(object):
    def canWin(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) < 2:
            return False
        slist = list(s)
        return self.canwin(slist, True)
        
    # player 1 True, 2 False
    def canwin(self, slist, player):
        for i in range(len(slist)-1):
            if slist[i] == "+" and slist[i+1] == "+":
                slist[i] = '-'
                slist[i+1] = '-'
                oppo = self.canwin(slist, not player)
                slist[i] = '+'
                slist[i+1] = '+'
                if not oppo:
                    return True
                
        return False
        
"""
class Solution(object):
    def canWin(self, s):
        memo = {}
        def can(piles):
            piles = tuple(sorted(p for p in piles if p >= 2))
            if piles not in memo:
                memo[piles] = any(not can(piles[:i] + (j, pile-2-j) + piles[i+1:])
                                  for i, pile in enumerate(piles)
                                  for j in range(pile - 1))
            return memo[piles]
        return can(map(len, re.findall(r'\+\++', s)))
"""