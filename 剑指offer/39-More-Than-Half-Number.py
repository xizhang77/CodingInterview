# -*- coding: utf-8 -*-

'''
// 面试题39：数组中出现次数超过一半的数字
// 题目：数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。例
// 如输入一个长度为9的数组{1, 2, 3, 2, 2, 2, 5, 4, 2}。由于数字2在数组中
// 出现了5次，超过数组长度的一半，因此输出2。

同LeetCode 169: https://leetcode.com/problems/majority-element/
'''

# Time: O(nlogn); Space: O(1)
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted( nums )
        
        return nums[ len(nums)/2 ]


# Time O(n); Space: O(1)
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return
        
        ans = nums[0]
        count = 1
        for num in nums[1:]:
            if num == ans:
                count += 1
            else:
                count -= 1
            
            if count < 0:
                ans = num
                count = 1
                
        return ans