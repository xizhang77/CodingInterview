# -*- coding: utf-8 -*-

'''
// 面试题31：栈的压入、弹出序列
// 题目：输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是
// 否为该栈的弹出顺序。假设压入栈的所有数字均不相等。例如序列1、2、3、4、
// 5是某栈的压栈序列，序列4、5、3、2、1是该压栈序列对应的一个弹出序列，但
// 4、3、5、1、2就不可能是该压栈序列的弹出序列。
'''

class Solution(object):     
	def isPopOrder(self, pushorder, poporder):
		"""
		:type pushorder: List[int]
		:type poporder: List[int]
		:rtype: bool
		"""
		stack = []

		while poporder:
			val = poporder.pop(0)

			if (not pushorder) and stack and stack[-1] != val:
				return False

			while pushorder and ( not stack or stack[-1] != val):
				stack.append( pushorder.pop(0) )

			if stack and stack[-1] == val:
				stack.pop()

		return not pushorder


s = Solution()
print s.isPopOrder( [1, 2, 3, 4, 5], [3, 5, 4, 1, 2] ) #False
print s.isPopOrder( [1, 2, 3, 4, 5], [4, 3, 5, 1, 2] ) #False
print s.isPopOrder( [1, 2, 3, 4, 5], [3, 5, 4, 2, 1] ) #True