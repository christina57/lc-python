"""
624. Maximum Distance in Arrays

Given m arrays, and each array is sorted in ascending order. Now you can pick up two integers from two different arrays (each array picks one) and calculate the distance. We define the distance between two integers a and b to be their absolute difference |a-b|. Your task is to find the maximum distance.

Example 1:
Input: 
[[1,2,3],
 [4,5],
 [1,2,3]]
Output: 4
Explanation: 
One way to reach the maximum distance 4 is to pick 1 in the first or third array and pick 5 in the second array.
Note:
Each given array will have at least 1 number. There will be at least two non-empty arrays.
The total number of the integers in all the m arrays will be in the range of [2, 10000].
The integers in the m arrays will be in the range of [-10000, 10000].
"""

class Solution(object):
    def maxDistance(self, arrays):
        """
        :type arrays: List[List[int]]
        :rtype: int
        """
        min1 = [sys.maxsize, 0]
        min2 = [sys.maxsize, 0]
        max1 = [-sys.maxsize, 0]
        max2 = [-sys.maxsize, 0]
        
        for i, arr in enumerate(arrays):
            if arr[0] < min1[0]:
                min2 = min1
                min1 = [arr[0], i]
            elif arr[0] < min2[0]:
                min2 = [arr[0], i]
            
            if arr[-1] > max1[0]:
                max2 = max1
                max1 = [arr[-1], i]
            elif arr[-1] > max2[0]:
                max2 = [arr[-1], i]
        
        if min1[1] == max1[1]:
            return max(max1[0] - min2[0], max2[0] - min1[0])
        else:
            return max1[0] - min1[0]
                
                
        