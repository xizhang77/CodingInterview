# -*- coding: utf-8 -*-

'''
// 面试题42：连续子数组的最大和
// 题目：输入一个整型数组，数组里有正数也有负数。数组中一个或连续的多个整
// 数组成一个子数组。求所有子数组的和的最大值。要求时间复杂度为O(n)。


同LeetCode 53: https://leetcode.com/problems/maximum-subarray/
'''

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return
        
        ans = -float('inf')
        dp = [ 0 ]
        
        for num in nums:
            dp.append( max(num, num + dp[-1]) )
            ans = max( ans, dp[-1] )
        
        return ans