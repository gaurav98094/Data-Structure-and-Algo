'''
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.

 

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Example 2:

Input: nums = [1]
Output: 1
Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23
'''



class Solution:
    def maxSubArray(self, a: List[int]) -> int:
        max_so_far =a[0]
        curr_max = a[0]
     
        for i in range(1,len(a)):
            curr_max = max(a[i], curr_max + a[i])
            max_so_far = max(max_so_far,curr_max)
             
        return max_so_far