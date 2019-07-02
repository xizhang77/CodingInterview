# -*- coding: utf-8 -*-

'''
// 面试题21：调整数组顺序使奇数位于偶数前面
// 题目：输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有
// 奇数位于数组的前半部分，所有偶数位于数组的后半部分。
'''

# Solution 1: Brute Force
# Time: O(n); Space: O(n)
class Solution1(object):
	def reOrder(self, nums):
		"""
		:type nums: array
		:rtype: array
		"""
		odd, even = [], []

		for num in nums:
			if num%2 == 0:
				even.append( num )
			else:
				odd.append( num )

		return odd + even


# Solution 2: Two Pointer
# Time: O(n); Space: O(1)
class Solution2(object):
	def reOrder(self, nums):
		"""
		:type nums: array
		:rtype: array
		"""
		n = len(nums)

		p, q = 0, n - 1

		i = 0
		while p < q:
			if nums[i]%2 == 0:
				nums[i], nums[q] = nums[q], nums[i]
				q -= 1
			else:
				p += 1
				i += 1

		return nums

s = Solution2()

print s.reOrder( [2, 4, 6, 1, 3, 5, 7] )
print s.reOrder( range(1, 8) )
print s.reOrder( [2, 4, 6, 1, 3, 5, 7] )
