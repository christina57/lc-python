"""
360. Sort Transformed Array

Given a sorted array of integers nums and integer values a, b and c. Apply a function of the form f(x) = ax2 + bx + c to each element x in the array.

The returned array must be in sorted order.

Expected time complexity: O(n)

Example:
nums = [-4, -2, 2, 4], a = 1, b = 3, c = 5,

Result: [3, 9, 15, 33]

nums = [-4, -2, 2, 4], a = -1, b = 3, c = 5

Result: [-23, -5, 1, 7]
Credits:
"""
"""
a>0，说明两端的值比中间的值大，那么此时我们从结果res后往前填数，用两个指针分别指向nums数组的开头和结尾，指向的两个数就是抛物线两端的数，将它们之中较大的数先存入res的末尾，然后指针向中间移，重复比较过程，直到把res都填满。

当a<0，说明两端的值比中间的小，那么我们从res的前面往后填，用两个指针分别指向nums数组的开头和结尾，指向的两个数就是抛物线两端的数，将它们之中较小的数先存入res的开头，然后指针向中间移，重复比较过程，直到把res都填满。

当a=0，函数是单调递增或递减的，那么从前往后填和从后往前填都可以，我们可以将这种情况和a>0合并
"""

class Solution(object):
    def sortTransformedArray(self, nums, a, b, c):
        """
        :type nums: List[int]
        :type a: int
        :type b: int
        :type c: int
        :rtype: List[int]
        """
        length = len(nums)
        res = [0] * length
        idx = length-1 if a >=0 else 0
        
        start = 0
        end = length - 1
        while start <= end:
            s = self.func(nums[start],a,b,c)
            e = self.func(nums[end],a,b,c)
            if a >= 0:
                if s >= e:
                    res[idx] = s
                    start += 1
                else:
                    res[idx] = e
                    end -= 1
                idx -= 1
            else:
                if s >= e:
                    res[idx] = e
                    end -= 1
                else:
                    res[idx] = s
                    start += 1
                idx += 1
        return res    
        
    def func(self, num, a, b, c):
        return a*num*num + b*num + c