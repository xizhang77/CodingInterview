# -*- coding: utf-8 -*-

'''
// 面试题33：二叉搜索树的后序遍历序列
// 题目：输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。
// 如果是则返回true，否则返回false。假设输入的数组的任意两个数字都互不相同。

'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
	def dfs(self, postorder, target, flag):
		if not postorder:
			return True
		if (flag and max(postorder) > target) or (not flag and min(postorder) < target):
			return False
		val = postorder.pop()
		i = 0
		while i < len(postorder) and postorder[i] < val:
			i += 1

		return self.dfs( postorder[:i], val, 1 ) and self.dfs( postorder[i:], val, 0 )

	def SquenceOfBST(self, postorder):
		"""
		:type postorder: List[int]
		:rtype: bool
		"""
		return self.dfs( postorder, float('inf'), 1) 

s = Solution()
print s.SquenceOfBST( [5,7,6,9,11,10,8] ) # T
print s.SquenceOfBST( [4, 6, 7, 5] ) # T
print s.SquenceOfBST( [1, 2, 3, 4, 5] ) #T
print s.SquenceOfBST( [5, 4, 3, 2, 1] ) #T
print s.SquenceOfBST( [5, 4, 3, 2, 1] ) #T
print s.SquenceOfBST( [4, 6, 12, 8, 16, 14, 10] ) #F
print s.SquenceOfBST( [4] ) #F