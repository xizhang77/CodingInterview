# -*- coding: utf-8 -*-

'''
同LeetCode 153
https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
'''


class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
        	return
        if nums[0] < nums[-1]: # No rotation
        	return nums[0]

        i, j = 0, len(nums) - 1
        while i <= j:
        	if nums[i] <= nums[j]:
        		return nums[i]

        	mid = i + (j-i)/2

        	if nums[i] < nums[ mid ]:
        		i = mid + 1
        	else:
        		j = mid