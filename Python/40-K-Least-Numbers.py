# -*- coding: utf-8 -*-

'''
// 面试题40：最小的k个数
// 题目：输入n个整数，找出其中最小的k个数。例如输入4、5、1、6、2、7、3、8
// 这8个数字，则最小的4个数字是1、2、3、4。

Similar to LeetCode 215: https://leetcode.com/problems/kth-largest-element-in-an-array/
'''

# Time: O(nlogk); Space: O(k)
import heapq
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if not nums:
            return
        
        stack = []
        
        for num in nums:
            heapq.heappush( stack, -num )
            if len(stack) > k:
                heapq.heappop( stack )
        
        
        return [ - num for num in stack ]