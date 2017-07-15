"""
259. 3Sum Smaller

Given an array of n integers nums and a target, find the number of index triplets i, j, k with 0 <= i < j < k < n that satisfy the condition nums[i] + nums[j] + nums[k] < target.

For example, given nums = [-2, 0, 1, 3], and target = 2.

Return 2. Because there are two triplets which sums are less than 2:

[-2, 0, 1]
[-2, 0, 3]
Follow up:
Could you solve it in O(n2) runtime?

"""

class Solution(object):
    def threeSumSmaller(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        lens = len(nums)
        if lens < 3:
            return 0
        
        list.sort(nums)
        res = 0
        
        for i in range(lens-2):
            left = i+1
            right = lens -1
            targ = target - nums[i]
            
            while left < right:
                if nums[left] + nums[right] >= targ:
                    right -= 1
                else:
                    res += (right - left)
                    left += 1
        
        return res
                
        