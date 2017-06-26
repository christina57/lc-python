"""
548. Split Array with Equal Sum

Given an array with n integers, you need to find if there are triplets (i, j, k) which satisfies following conditions:

0 < i, i + 1 < j, j + 1 < k < n - 1
Sum of subarrays (0, i - 1), (i + 1, j - 1), (j + 1, k - 1) and (k + 1, n - 1) should be equal.
where we define that subarray (L, R) represents a slice of the original array starting from the element indexed L to the element indexed R.
Example:
Input: [1,2,1,2,1,2,1]
Output: True
Explanation:
i = 1, j = 3, k = 5. 
sum(0, i - 1) = sum(0, 0) = 1
sum(i + 1, j - 1) = sum(2, 2) = 1
sum(j + 1, k - 1) = sum(4, 4) = 1
sum(k + 1, n - 1) = sum(6, 6) = 1
Note:
1 <= n <= 2000.
Elements in the given array will be in range [-1,000,000, 1,000,000].
"""

class Solution(object):
    def splitArray(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        nlen = len(nums) 
        if nlen < 7:
            return False
            
        presum = [0] * nlen
        postsum = [0] * nlen
        
        for i, n in enumerate(nums):
            presum[i] = (presum[i-1] if i > 0 else 0) + n
        
        for i in range(nlen-1, -1, -1):
            postsum[i] = (postsum[i+1] if i < nlen-1 else 0) + nums[i]
            
        for i in range(1, nlen-5):
            for k in range(nlen-2, 4, -1):
                if presum[i-1] == postsum[k+1]:
                    temp = presum[nlen-1] + nums[i] + nums[k] - 2 * presum[i] - 2 * postsum[k]
                    for j in range(i+2, k-1):
                        if nums[j] == temp:
                            return True
                        
        return False