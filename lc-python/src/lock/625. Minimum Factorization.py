"""

625. Minimum Factorization

Given a positive integer a, find the smallest positive integer b whose multiplication of each digit equals to a.

If there is no answer or the answer is not fit in 32-bit signed integer, then return 0.

Example 1
Input:

48 
Output:
68
Example 2
Input:

15
Output:
35

"""

class Solution(object):
    def smallestFactorization(self, a):
        """
        :type a: int
        :rtype: int
        """
        if a < 1:
            return 0
        if a == 1:
            return 1
        cur = a
        res = 0
        muti = 1
        for i in range(9, 1, -1):
            while cur % i == 0:
                cur /= i
                res += i * muti
                muti *= 10
        if cur > 1 or res > 2**31:
            return 0
        else:
            return res
        